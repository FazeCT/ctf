## Introduction

Lời đầu tiên, mình (FazeCT) - một thành viên của team RE trong câu lạc bộ An toàn thông tin HCMUT (BKISC) xin gửi lời chào đến các bạn đang đọc bài viết!

Trong bài viết này, mình sẽ giúp các bạn hiểu được basics của mảng Reverse Engineering - RE, một trong 4 mảng chính của CTF.

Trước khi vào Write-Up, mình muốn các bạn thử đọc qua slide sau đây để nắm rõ thuật ngữ cơ bản trong RE, cũng như hiểu được một trong những dạng bài của RE, đó là Unity RE: [go to slide](https://docs.google.com/presentation/d/10Z2u5gLyN5w5rhyMwWNFmZaDFL8Nbbjfsqf0z8HDsUc/edit?usp=sharing)

Sau đây sẽ là Write-Up của một bài Unity RE đến từ **SEKAI CTF 2022**.

## Information
**Category** | **Writeup Author**
--- | ---
Reverse Engineering | FazeCT

**Description:** 

(Challenge từ SEKAI CTF 2022)

[...] Giành chiến thắng trong trò chơi mô phỏng lại dựa trên tựa game [Fall Guy](https://vi.wikipedia.org/wiki/Fall_Guys).

(Insert link zip)

## First Observation

Để thuận tiện cho các bạn mới tìm hiểu về mảng RE, mình sẽ mở đầu bằng cách phân tích về những file trong zip.

Như đã đề cập đến trong slide phía trên, 2 folder sẽ chứa tài nguyên của game và file thực thi .exe sẽ là game chúng ta cần crack.

Mình tiến hành mở .exe lên chơi thử, cách vận hành của game này được lấy ý tưởng từ màn chơi [Perfect Match](https://fallguysultimateknockout.fandom.com/wiki/Perfect_Match) của tựa game Fall Guy.

(Insert video chơi thử)

Để có được flag, ta cần vượt qua màn chơi này mà không bị rơi xuống phía dưới.

## Solution

Sử dụng các tool (dnSpy, dotPeek hay IDA) như trong slide có đề cập đến để decompile file **Assembly-CSharp.dll** chứa trong đường dẫn **.../Perfect_Match_X-treme/Build/PerfectMatch_Data/Managed/Assembly-CSharp.dll**



> Flag is: ...
