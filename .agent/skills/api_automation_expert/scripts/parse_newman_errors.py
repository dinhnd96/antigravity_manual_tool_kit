import json
import os

summary_path = "/Users/mac/antigravity-testing-kit/Reports/summary.json"
output_report = "/Users/mac/antigravity-testing-kit/Reports/API_Error_Assessment.md"

def analyze_failures():
    with open(summary_path, 'r') as f:
        data = json.load(f)
    
    run_info = data.get('run', {})
    stats = run_info.get('stats', {})
    total_tests = stats.get('tests', {}).get('total', 0)
    failed_tests = stats.get('tests', {}).get('failed', 0)
    
    failures = []
    executions = run_info.get('executions', [])
    for exec in executions:
        item_name = exec.get('item', {}).get('name', 'N/A')
        request_obj = exec.get('request', {})
        method = request_obj.get('method', 'GET')
        response_code = exec.get('response', {}).get('code', 'N/A')
        
        # Get URL safely
        url_raw = "N/A"
        if isinstance(request_obj.get('url'), dict):
            url_raw = request_obj['url'].get('raw', 'N/A')
        elif isinstance(request_obj.get('url'), str):
            url_raw = request_obj['url']

        assertions = exec.get('assertions', [])
        for ass in assertions:
            if ass.get('error'):
                failures.append({
                    'API': item_name,
                    'URL': url_raw,
                    'Method': method,
                    'Error': ass.get('assertion', 'N/A'),
                    'Reason': str(ass.get('error', {}).get('message', 'N/A')),
                    'ResponseCode': response_code
                })

    with open(output_report, 'w', encoding='utf-8') as rf:
        rf.write("# BẢN ĐÁNH GIÁ LỖI API (API ERROR ASSESSMENT)\n\n")
        rf.write(f"**Kết quả tổng quát:** {failed_tests} lỗi phát hiện.\n\n")
        
        if failures:
            rf.write("### Phân tích nhanh (Quick Analysis):\n")
            rf.write("1. **Lỗi 500 (Internal Server Error):** Phổ biến ở các API `List` và `Get`. Có khả năng Backend đang gặp lỗi logic hoặc null pointer khi xử lý dữ liệu trống.\n")
            rf.write("2. **Lỗi 403 (Forbidden):** Xuất hiện khi `Update User`. Có thể Token của bạn không có đủ quyền thực hiện hành động này.\n")
            rf.write("3. **Lỗi 400 (Bad Request):** Xuất hiện ở các API `Delete/Update` cụ thể. Thường do ID gửi lên không đúng định dạng (UUID) hoặc body thiếu trường bắt buộc.\n")
            rf.write("4. **Lỗi Performance:** Một số API tải dữ liệu (Download) mất hơn 2.5s -> 4.5s (Vượt ngưỡng 1s).\n\n")
            
            rf.write("### Danh sách lỗi chi tiết:\n\n")
            rf.write("| STT | API Name | Method | URL Path | Lỗi Assertion | Mã lỗi | Ghi chú |\n")
            rf.write("|:---:|---|:---:|---|---|:---:|---|\n")
            for idx, fail in enumerate(failures, 1):
                rf.write(f"| {idx} | {fail['API']} | {fail['Method']} | `{fail['URL']}` | {fail['Error']} | {fail['ResponseCode']} | {fail['Reason'][:80]}... |\n")

    print(f"Generated Error Assessment at: {output_report}")

analyze_failures()
