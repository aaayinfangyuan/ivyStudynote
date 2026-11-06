from __future__ import annotations

import json
import mimetypes
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parent
NOTES = ROOT / "notes"
HOST = "127.0.0.1"
PORT = 8765

class NotesHandler(SimpleHTTPRequestHandler):
    # Serve all project files from the project folder.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def do_POST(self):
        path = unquote(urlparse(self.path).path)
        prefix = "/api/notes/"
        if not path.startswith(prefix):
            self.send_error(HTTPStatus.NOT_FOUND, "Unknown API endpoint")
            return
        filename = path[len(prefix):]
        # Only permit one Markdown filename in notes/, never arbitrary paths.
        if not filename.endswith(".md") or Path(filename).name != filename:
            self.send_error(HTTPStatus.BAD_REQUEST, "Invalid note filename")
            return
        target = (NOTES / filename).resolve()
        if target.parent != NOTES.resolve() or not target.exists():
            self.send_error(HTTPStatus.NOT_FOUND, "Note not found")
            return
        try:
            size = int(self.headers.get("Content-Length", "0"))
            if size <= 0 or size > 1_000_000:
                raise ValueError
            payload = json.loads(self.rfile.read(size).decode("utf-8"))
            markdown = payload["markdown"]
            if not isinstance(markdown, str):
                raise ValueError
        except (ValueError, UnicodeDecodeError, json.JSONDecodeError, KeyError):
            self.send_error(HTTPStatus.BAD_REQUEST, "Expected JSON: {markdown: string}")
            return
        # Write a real Markdown file. Git and VS Code will see this exact change.
        target.write_text(markdown.rstrip() + "\n", encoding="utf-8")
        data = json.dumps({"ok": True, "file": filename}, ensure_ascii=False).encode("utf-8")
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

if __name__ == "__main__":
    print(f"\nPython 学习笔记已启动： http://{HOST}:{PORT}/")
    print("网页保存会直接修改 notes/ 中的 Markdown 文件。")
    print("按 Ctrl + C 停止服务。\n")
    ThreadingHTTPServer((HOST, PORT), NotesHandler).serve_forever()
