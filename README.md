# Onichan-Baka-vcode (Gọi tắt: `Oni-VCode`)

> **Bộ Skill AI Thượng Đẳng Tự Động Ngầm (Passive Always-On) + Bộ Độ Giao Diện Anime Động Cho Desktop & Terminal AI**
> Tương thích xuyên suốt mọi nền tảng AI (**Claude Code, Claude Desktop, OpenAI Codex / ChatGPT Desktop, Cursor, Gemini CLI, Antigravity, Windsurf, OpenCode, Kiro**).

---

## 1. Cách gọi nhanh & Cơ chế Bị động 100% (Passive vs. Active)

- **Tên đầy đủ của Skill**: `onichan-baka-vcode` (**Onichan-Baka-vcode**)
- **Tên gọi tắt kích hoạt nhanh**: **`Oni-VCode`** (hoặc `/oni-vcode`, `/oni-theme`, `/rea`)

| Phân hệ trong `Oni-VCode` | Chế độ hoạt động | Mô tả |
| :--- | :--- | :--- |
| **1. Bộ nhớ Vĩnh cửu & Bàn giao 0-Prompt (`.ai-memory/`)** | **BỊ ĐỘNG (Tự chạy ngầm 100%)** | Tự đọc `HANDOFF.md` & `BUG_LEDGER.md` mỗi khi mở app; hết quota hãng này nhảy sang hãng khác chỉ cần gõ `"tiếp tục"`. |
| **2. Điều phối Web 3 bước qua MCP 2026 (`mcp__*`)** | **BỊ ĐỘNG (Tự chạy ngầm 100%)** | Tự động Tìm kiếm đa nguồn ([Aas-ee/open-webSearch](https://github.com/aas-ee/open-websearch)) -> Cào Markdown 3-5 trang siêu tốc ([Fetch MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch), [Jina Reader MCP](https://github.com/jina-ai/MCP), [Crawl4AI](https://github.com/unclecode/crawl4AI)) -> Thao tác trình duyệt thật ([Microsoft Playwright MCP](https://github.com/microsoft/playwright-mcp)). |
| **3. Phân tích sâu 360 độ & Kỹ sư Trưởng 30-50 năm** | **BỊ ĐỘNG (Tự chạy ngầm 100%)** | Tự động mở rộng prompt ngắn thành bản thiết kế hoàn chỉnh, tự bắt edge cases, race conditions và tối ưu hiệu năng. |
| **4. Đội ngũ Công ty Đa Agent GStack & Bảo mật `/cso`** | **BỊ ĐỘNG (Tự chạy ngầm 100%)** | Tự động vận hành quy trình [garrytan/gstack](https://github.com/garrytan/gstack) (CEO, Eng Manager, Designer chống AI-slop, Staff Bug Hunter, QA, CSO kiểm thử OWASP/STRIDE & chịu tải cục bộ). |
| **5. Tạo, Tải Model & Render 3D ([ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender))** | **BỊ ĐỘNG (Tự nhận diện 3D)** | Tự động kích hoạt khi prompt có yêu cầu về 3D, Blender, Poly Haven, Poly Pizza, Meshy, Tripo, Hunyuan3D, World Labs. |
| **6. Dịch ngược REA ([morluto/rea](https://github.com/morluto/rea))** | **CHỦ ĐỘNG (Chỉ chạy khi gọi)** | **Mặc định ngủ đông.** Chỉ kích hoạt khi bạn chủ động yêu cầu dịch ngược binary/app/APK hoặc gõ `/rea`. |
| **7. Độ Giao diện Anime Động & Font Anime Script (`apply_anime_theme.py`)** | **HỎI HOẶC TỰ KICK (`ask` / `auto-kick`)** | Tự động thay 2 ảnh nền Anime của bạn + hiệu ứng lá bay/ánh sao động + [Anime Script Font](https://befonts.com/anime-script-font.html) vào Claude/Codex Desktop & Terminal, hỗ trợ hỏi hoặc tự kick phiên Codex để nạp giao diện ngay lập tức. |

---

## 2. Tính năng Độ Giao Diện Anime Động & Font Chữ Anime (`scripts/apply_anime_theme.py`)

Bộ skill đóng gói sẵn **2 bức ảnh Anime của bạn** trong `assets/wallpapers/`:
- `theme_1_cliff_swordsman.jpg`: Kiếm sĩ đứng trên vách đá nhìn xuống dòng sông với hiệu ứng lá xanh bay và nấm phát quang.
- `theme_2_moonlight_dualblade.jpg`: Nữ kiếm sĩ song kiếm dưới ánh trăng xanh cùng hiệu ứng hoa anh đào và bụi sao lấp lánh.
- **Font chữ Anime**: Tích hợp cấu hình font **[Anime Script Font](https://befonts.com/anime-script-font.html)** (`Anime-BF64c3cadb515c9.otf` của `andikastudio`) cho toàn bộ tiêu đề, thanh trạng thái và giao diện chat.

### Lệnh chạy chế độ Hỏi trước khi đổi (`--mode ask`):
```bash
python3 scripts/apply_anime_theme.py --mode ask --target all
```

### Lệnh chạy chế độ Tự động Đá (Auto-Kick) khỏi Codex/Terminal để nạp giao diện ngay (`--mode auto-kick`):
```bash
ONI_VCODE_FORCE_KICK=1 python3 scripts/apply_anime_theme.py --mode auto-kick --target all
```
*(Trước khi kick phiên để nạp giao diện, script tự động lưu toàn bộ trạng thái đang làm dở vào `.ai-memory/HANDOFF.md` để khi mở lại AI làm tiếp ngay mà không mất một dòng code nào!)*
