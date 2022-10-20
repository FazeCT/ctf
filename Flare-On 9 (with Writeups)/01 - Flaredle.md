# __Flare-On 9__ 
## _01 - Flaredle_

## Information
**Category** | **Points** | **Writeup Author**
--- | --- | ---
Reverse Engineering | 1 | FazeCT

**Description:** 

Welcome to Flare-On 9!

You probably won't win. Maybe you're like us and spent the year playing Wordle. We made our own version that is too hard to beat without cheating.

Play it live at: http://flare-on.com/flaredle/

## Solution
Đầu tiên, từ source 7z, unzip thu được được 2 file .js và 1 file .css, ta mở lên xem thử thì thấy:
- File word.js chứa kha khá từ, chắc là word cần sử dụng cho challenge này.
- File script.js chứa source của checker.

Đọc qua source script.js ta thấy số lần dự đoán tối đa là 6, nên chắc chắn ko thể brute tất cả trong 1 lần chơi.
Bỏ qua các hàm khởi tạo, ta bước thẳng vào checkGuess()

Nhận thấy source code có cho rightGuessString nằm ở index 57 của list, chính là flareonisallaboutcats, submit thử thì đúng luôn :))

![Result](Images/image_2022-10-01_094725006.png)

> Flag is: flar<span>eonisallaboutcats@flar</span>e-on.com
