# (1) Phân tích – Thiết kế giải pháp
# ---------------------------------------------------------
# Hàm phụ trợ:
# - find_patient_index(records, patient_id)
#   Input: records (list các chuỗi), patient_id (string)
#   Output: index hoặc -1
#   Luồng xử lý: chuẩn hóa patient_id (strip, upper), duyệt records, nếu chuỗi bắt đầu bằng patient_id thì trả về index.

# Hàm chính:
# - display_records(records)
#   Input: records (list các chuỗi)
#   Output: None (in ra màn hình)
#   Luồng xử lý: nếu list rỗng thì báo không có dữ liệu, ngược lại duyệt từng chuỗi, split("-"), in ra bảng.

# - add_patient(records)
#   Input: records (list các chuỗi)
#   Output: None (thêm hồ sơ mới vào list nếu hợp lệ)
#   Luồng xử lý:
#       Nhập mã BN, tên, năm sinh, chẩn đoán.
#       Chuẩn hóa:
#           Mã BN: strip() + upper()
#           Tên BN: strip() + title(), thay "-" bằng " "
#           Năm sinh: kiểm tra isdigit(), nằm trong [1900, năm hiện tại]
#           Chẩn đoán: strip() + capitalize(), thay "-" bằng " "
#       Kiểm tra trùng mã bằng find_patient_index.
#       Nếu hợp lệ thì ghép thành chuỗi "Mã-Tên-Năm-Chẩn đoán" và append().

# - update_diagnosis(records)
#   Input: records (list các chuỗi)
#   Output: None (cập nhật chẩn đoán bệnh)
#   Luồng xử lý:
#       Nhập mã BN, tìm index bằng find_patient_index.
#       Nếu không thấy thì báo lỗi.
#       Nếu thấy thì split chuỗi thành list, nhập chẩn đoán mới, chuẩn hóa, gán vào phần tử cuối.
#       Ghép lại thành chuỗi mới và gán đè vào records[index].

# - generate_age_report(records)
#   Input: records (list các chuỗi)
#   Output: None (in báo cáo phân loại tuổi)
#   Luồng xử lý:
#       Duyệt records, split để lấy năm sinh, tính tuổi = năm hiện tại - năm sinh.
#       Phân loại:
#           Tuổi < 16 → trẻ em
#           16 <= Tuổi <= 60 → trưởng thành
#           Tuổi > 60 → cao tuổi
#       Đếm số lượng, in báo cáo.

# Giải pháp tổng thể:
# - Truyền records vào hàm là truyền tham chiếu (reference), nên các hàm thao tác trực tiếp trên list gốc.
# - String là immutable, nên mọi chuẩn hóa phải gán lại.
# - List là mutable, nên append() hoặc gán index sẽ thay đổi trực tiếp danh sách.
# ---------------------------------------------------------

import datetime

patient_records = [
    "BN001-Nguyen Van A-1985-Viem Phoi",
    "BN002-Tran Thi B-1990-Sot Xuat Huyet",
    "BN003-Le Van C-2015-Viem Phe Quan"
]

def find_patient_index(records, patient_id):
    pid = patient_id.strip().upper()
    for i, rec in enumerate(records):
        if rec.startswith(pid + "-"):
            return i
    return -1

def display_records(records):
    if not records:
        print("Hệ thống hiện chưa có hồ sơ nào.")
    else:
        print("--- DANH SÁCH BỆNH NHÂN --------------------------------------------------")
        for i, rec in enumerate(records, start=1):
            parts = rec.split("-")
            print(f"{i}. [{parts[0]}] {parts[1]:15} | Năm sinh: {parts[2]} | Chẩn đoán: {parts[3]}")
        print("--------------------------------------------------------------------------")

def add_patient(records):
    print("--- THÊM HỒ SƠ BỆNH NHÂN MỚI ---")
    pid = input("Nhập mã bệnh nhân: ").strip().upper()
    if not pid:
        print("Mã bệnh nhân không được để trống!")
        return
    if find_patient_index(records, pid) != -1:
        print("Mã bệnh nhân đã tồn tại!")
        return
    name = input("Nhập tên bệnh nhân: ").strip().replace("-", " ").title()
    if not name:
        print("Tên bệnh nhân không được để trống!")
        return
    year = input("Nhập năm sinh: ").strip()
    current_year = datetime.datetime.now().year
    if not year.isdigit() or not (1900 <= int(year) <= current_year):
        print("Năm sinh không hợp lệ, vui lòng nhập lại!")
        return
    diagnosis = input("Nhập chẩn đoán: ").strip().replace("-", " ").capitalize()
    if not diagnosis:
        print("Chẩn đoán không được để trống!")
        return
    new_record = f"{pid}-{name}-{year}-{diagnosis}"
    records.append(new_record)
    print("Thêm hồ sơ bệnh nhân thành công!")

def update_diagnosis(records):
    print("--- CẬP NHẬT CHẨN ĐOÁN THEO MÃ BN ---")
    pid = input("Nhập mã bệnh nhân cần cập nhật: ").strip().upper()
    idx = find_patient_index(records, pid)
    if idx == -1:
        print(f"Không tìm thấy bệnh nhân mang mã {pid}!")
        return
    parts = records[idx].split("-")
    print(f"Tìm thấy bệnh nhân: {parts[1]}")
    print(f"Chẩn đoán hiện tại: {parts[3]}")
    new_diag = input("Nhập chẩn đoán mới: ").strip().replace("-", " ").capitalize()
    if not new_diag:
        print("Chẩn đoán không được để trống!")
        return
    parts[3] = new_diag
    records[idx] = "-".join(parts)
    print("Cập nhật chẩn đoán thành công!")

def generate_age_report(records):
    print("--- BÁO CÁO PHÂN LOẠI THEO ĐỘ TUỔI ---")
    current_year = datetime.datetime.now().year
    child = adult = elder = 0
    for rec in records:
        parts = rec.split("-")
        year = int(parts[2])
        age = current_year - year
        if age < 16:
            child += 1
        elif age <= 60:
            adult += 1
        else:
            elder += 1
    print(f"Trẻ em: {child} bệnh nhân")
    print(f"Trưởng thành: {adult} bệnh nhân")
    print(f"Người cao tuổi: {elder} bệnh nhân")
    print("--------------------------------------")

# Vòng lặp chính
while True:
    print("\n===== HỆ THỐNG QUẢN LÝ BỆNH ÁN RIKKEI HOSPITAL =====")
    print("1. Xem danh sách hồ sơ bệnh án")
    print("2. Thêm hồ sơ bệnh nhân mới")
    print("3. Cập nhật chẩn đoán theo Mã BN")
    print("4. Báo cáo phân loại theo độ tuổi")
    print("5. Thoát chương trình")
    choice = input("Chọn chức năng (1-5): ")
    if choice == "1":
        display_records(patient_records)
    elif choice == "2":
        add_patient(patient_records)
    elif choice == "3":
        update_diagnosis(patient_records)
    elif choice == "4":
        generate_age_report(patient_records)
    elif choice == "5":
        print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")
