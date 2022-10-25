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

(Insert hình files)

Mình tiến hành mở .exe lên chơi thử, cách vận hành của game này được lấy ý tưởng từ màn chơi [Perfect Match](https://fallguysultimateknockout.fandom.com/wiki/Perfect_Match) của tựa game Fall Guy.

(Insert video chơi thử)

Để có được flag, ta cần vượt qua màn chơi này mà không bị rơi xuống phía dưới.

## Solution

Sử dụng các tool (dnSpy, dotPeek hay IDA) như trong slide có đề cập đến để decompile file **Assembly-CSharp.dll** chứa trong đường dẫn **.../Perfect_Match_X-treme/Build/PerfectMatch_Data/Managed/Assembly-CSharp.dll**

Sau khi decompile, ban đầu ta sẽ thấy cửa sổ như sau trong dnSpy:

(Insert hình dnspy1)

Ở phía bên trái, ta có một cửa sổ hiển thị danh sách các thành phần của file **Assembly-CSharp.dll**.

(Insert hình dnspy2)

Toàn bộ phần màu xanh chính là các **GameObject** mà mình đã đề cập đến trong slide ở phía trên, trong đó có **GameManager** mà ta có thể nói rằng nó là main để vận hành trò chơi.

(Insert hình dnspy3)

Trên đây là cấu trúc của **GameManager** được decompile thành pseudocode của ngôn ngữ **C#**. Mỗi hàm của **GameManager** đều có một chức năng riêng, như 
**ChooseBasedOnRound()** là hàm để setup mỗi round, hay **ChooseFruit()** cũng là một hàm để setup platform của màn chơi. Tuy nhiên, ta nhận thấy có một hàm tên là **IncreaseRound()** dùng để kiểm tra tiến độ game mà trong đó ta thấy dòng lệnh **isGameOver = true;**, đây có thể hiểu là câu lệnh dùng để kết thúc game.

```
public void IncreaseRound()
{
	if (this.roundNumber + 1 <= 3)
	{
		this.roundNumber++;
		base.StartCoroutine("CheckRound");
		return;
	} //sau khi vượt qua 3 round đấu, game sẽ kết thúc.
	this.isGameOver = true;
}
```
Thử edit class để bỏ dòng lệnh **this.isGameOver = true;** lên trên đầu class, tức ngay trong **void Awake()**. Cách thức edit class đã được mình hướng dẫn trong slide phía trên.

**Lưu ý:** Trong quá trình edit class, nếu các bạn gặp một vài lỗi compile như mình thì có thể vứt luôn đoạn code bị lỗi đó, vì mục tiêu của mình là chỉ chạy đến **void Awake()** là đã kết thúc chương trình.

(Insert dnspy4)

Sau khi compile xong, ta tiến hành save module, lưu đè lên file **.dll** gốc (nên backup file **.dll** gốc).

(Insert dnspy5)

> Flag is: ...
