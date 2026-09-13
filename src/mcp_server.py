"""
🔌 MODEL CONTEXT PROTOCOL (MCP) SERVER MODULE
Mô phỏng kiến trúc MCP Server (Client-Server Architecture) cung cấp công cụ chuẩn hóa.
"""

import json
import sys
from typing import Dict, Any, List
from tools import TOOLS_SCHEMA, dispatch_tool_call

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

class MCPAcademicServer:
    """
    Giả lập MCP Server tuân thủ chuẩn giao thức Model Context Protocol
    """
    def __init__(self, server_name: str = "vinuni-academic-mcp-server"):
        self.server_name = server_name
        self.version = "2026.1.0"
        
    def list_tools(self) -> List[Dict[str, Any]]:
        """Trả về danh sách các Tools chuẩn giao thức MCP"""
        return TOOLS_SCHEMA
        
    def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """
        [TASK 2.1] HỌC VIÊN HOÀN THIỆN HÀM THỰC THI TOOL TRÊN MCP SERVER
        Thực thi request gọi Tool theo chuẩn MCP JSON-RPC
        """
        # 1. Gọi hàm dispatch_tool_call để lấy chuỗi JSON kết quả từ Tool Router
        raw_result = dispatch_tool_call(tool_name, arguments)
        
        # 2. Chuyển đổi chuỗi JSON kết quả thành Python Dictionary
        content = json.loads(raw_result)
        
        # 3. Đóng gói phản hồi và trả về Dict theo đúng chuẩn giao thức MCP JSON-RPC 2.0
        return {
            "jsonrpc": "2.0",
            "server": self.server_name,
            "tool": tool_name,
            "result": content
        }


if __name__ == "__main__":
    server = MCPAcademicServer()
    tools = server.list_tools()
    
    # 1. Kiểm tra số lượng tools đã đăng ký thành công
    if len(tools) >= 2:
        print(f"✅ [TOOLS CHECK]: Đã đăng ký thành công {len(tools)} Native Tools trong TOOLS_SCHEMA!")
    else:
        print(f"⏳ [TOOLS CHECK]: Chưa đăng ký đủ số lượng Native Tools.")

    # 2. Gọi thử nghiệm tool academic_query để lấy kết quả in ra màn hình
    try:
        test_result = server.call_tool("academic_query", {"student_id": "SV2026001"})
        status = test_result.get("result", {}).get("status", "FAILED")
        student_name = test_result.get("result", {}).get("data", {}).get("full_name", "Không rõ")
        
        # In ra dòng kết quả khớp hoàn toàn với mẫu thiết kế giao diện của bạn
        print(f"🧪 Kết quả gọi thử academic_query: Status {status} (Sinh viên {student_name})")
    except Exception as e:
        print(f"❌ Lỗi khi thực hiện kiểm thử gọi tool: {e}")

    # Kiểm tra trạng thái TODO 1.2 (Tool Schema)
    sched_tool = next((t for t in tools if t.get("name") == "schedule_appointment"), None)
    
    has_properties = False
    if sched_tool:
        schema_body = sched_tool.get("inputSchema") or sched_tool.get("parameters")
        if schema_body and schema_body.get("properties"):
            has_properties = True

    if not has_properties:
        print("⏳ [TODO 1.2]: Tool 'schedule_appointment' chưa được định nghĩa properties trong 'src/tools.py'.")
    else:
        print("✅ [TODO 1.2]: Tool 'schedule_appointment' đã có schema đầy đủ.")

    # Kiểm tra trạng thái TODO 2.1 (call_tool)
    if not test_result:
        print("⏳ [TODO 2.1]: Hàm call_tool() đang trả về rỗng. Học viên hãy hoàn thiện TODO 2.1 trong 'src/mcp_server.py'!")
    else:
        print(f"✅ [TODO 2.1]: Test dispatch tool 'academic_query' thành công:")
        print(f"   Phản hồi JSON-RPC: {json.dumps(test_result, ensure_ascii=False)}")
