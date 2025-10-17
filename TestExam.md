
# Chương 1: Tổng quan

**PAGE 13**  
Tổng quan  
An toàn và bảo mật thông tin

**PAGE 15**  
Tổng quan An toàn và bảo mật thông tin

**PAGE 16**  
Tổng quan An toàn và bảo mật thông tin

**PAGE 17**  
Tổng quan An toàn và bảo mật thông tin

**PAGE 18**  
Tổng quan An toàn và bảo mật thông tin

* Nội dung của an toàn và bảo mật thông tin:

> Khi như cấu trao đổi thông tin dữ liệu ngày càng lớn và đa dạng. Bảo vệ an toàn thông tin dữ liệu là một chủ đề rộng, có liên quan đến nhiều lĩnh vực.

**PAGE 19**  
Tổng quan An toàn và bảo mật thông tin
C. phương pháp bảo vệ ATTT dữ liệu có thể được quy tụ vào ba nhóm sau:
> Bảo vệ an toàn thông tin bằng các biện pháp hành chính.
> Bảo vệ an toàn thông tin bằng các biện pháp kỹ thuật (phần cứng).
> Bảo vệ an toàn thông tin bằng các biện pháp thuật toán (phần mềm).
=> Ba nhóm trên có thể được ứng dụng riêng rẽ hoặc phối kết hợp

**PAGE 20**  
Tổng quan An toàn và bảo mật thông tin

* Môi trường khó bảo vệ an toàn thông tin nhất và cũng là môi trường đối phương dễ xâm nhập nhất đó là môi trường mạng và truyền tin.
* Biện pháp hiệu quả nhất và kinh tế nhất hiện nay trên mạng truyền tin và mạng máy tính là biện pháp thuật toán.

**PAGE 21**  
Tổng quan An toàn và bảo mật thông tin

* An toàn thông tin bao gồm các nội dung sau:

> Tính bí mật: tính kín đáo riêng tư của thông tin
> Tính xác thực của thông tin, bao gồm xác thực đối tác (bài toán nhận danh), xác thực thông tin trao đổi.
> Tính trách nhiệm: đảm bảo người gửi thông tin không thể thoái thác trách nhiệm về thông tin mà mình đã gửi

**PAGE 22**  
Tổng quan An toàn và bảo mật thông tin
Đề đảm bảo ATTT dữ liệu trên đường truyền tin và trên mạng dự đoán trước các khả năng:
không an toàn,
khả năng xâm phạm,
các sự cố rủi ro có thể xảy ra đối với thông tin dữ liệu được lưu trữ và trao đổi trên đường truyền tin cũng như trên mạng.
xác định càng chính xác các nguy cơ nói trên thì càng quyết định được tốt các giải pháp để giảm thiểu các thiệt hại.

**PAGE 23**  
Tổng quan An toàn và bảo mật thông tin

* Có hai loại hành vi xâm phạm thông tin:

> Xâm phạm thụ động: liên quan đến việc nghe lén hoặc quan sát thông tin được truyền đi

* Tách nội dung thông điệp: thu các thông tin nhạy cảm trong thư điện tử hay trong các tập tin truyền đi.
* Phân tích đường truyền: thông tin nhạy cảm có thể được che dấu bằng mã hóa, nhưng đối thủ có thể xác định vị trí các thực thể và quan sát tần suất và độ dài của thông điệp để rút trích bản chất của thông điệp

**PAGE 24**  
Tổng quan An toàn và bảo mật thông tin
=>Xâm phạm thụ động khó phát hiện vì không có ảnh hưởng đến tài nguyên và thao tác của hệ thống -> tập trung phòng chống

**PAGE 25**  
Tổng quan An toàn và bảo mật thông tin

* Có hai loại hành vi xâm phạm thông tin:

> Xâm phạm chủ động: liên quan đến việc thay đổi dữ liệu hoặc tạo dữ liệu sai

* Giả mạo: thực hiện các thao tác theo sau một chứng thực hợp lệ để sử dụng các quyền của người dùng hợp lệ cho các thao tác "không hợp lệ" trong hệ thống.
* Làm lại (replay): truyền lại các gói tin của lần chứng thực hợp lệ của quá khứ cho các lần chứng thực trong tương lai.

**PAGE 26**  
Tổng quan An toàn và bảo mật thông tin

* Thay đổi thông điệp: một phần hoặc toàn bộ thông tin hợp pháp bị thay thế bằng các thông tin giả mạo nhằm thực hiện các tác vụ không cho phép.
* Từ chối dịch vụ (denial of service): ngăn chặn hay gây ức chế việc sử dụng và quản lý thông thường của các thiết bị truyền thông.
=>Để phát hiện nhưng khó ngăn chặn

**PAGE 27**  
Các chiến lược an toàn hệ thống
Giới hạn quyền hạn tối thiểu (Last Privilege):
Đây là chiến lược cơ bản nhất theo nguyên tắc này bất kỳ một đối tượng nào cũng chỉ có những quyền hạn nhất định đối với tài nguyên mạng, khi thẩm nhập vào mạng đối tượng đó chỉ được sử dụng một số tài nguyên nhất định.
Bảo vệ theo chiều sâu (Defence In Depth):
Nguyên tắc này nhắc nhở chúng ta: Không nên dựa vào một chế độ an toàn nào dù cho chúng rất mạnh, mà nên tạo nhiều cơ chế an toàn để tương hỗ lẫn nhau.

**PAGE 28**  
Các chiến lược an toàn hệ thống

* Nút thắt (Choke Point):

> Tạo ra một "cửa khẩu" hẹp, và chỉ cho phép thông tin đi vào hệ thống của mình bằng con đường duy nhất chính là "cửa khẩu" này.

* Điểm yếu nhất (Weakest Link):

> Chiến lược này dựa trên nguyên tắc: "Một dây xích chỉ chắc tại mắt duy nhất, một bức tường chỉ chắc tại điểm yếu nhất"
> Kẻ phá hoại thường tìm những chỗ yếu nhất của hệ thống để tấn công, do đó ta cần phải gia cố các yếu điểm của hệ thống.

**PAGE 29**  
Các chiến lược an toàn hệ thống

**PAGE 30**  
Các mức bảo vệ trên mạng

* Quyền truy nhập

> Lớp bảo vệ trong cùng là quyền truy nhập nhằm kiểm soát các tài nguyên của mạng và quyền hạn trên tài nguyên đó. Dĩ nhiên là kiểm soát được các cấu trúc dữ liệu càng chi tiết càng tốt. Hiện tại việc kiểm soát thường ở mức tệp

**PAGE 31**  
Các mức bảo vệ trên mạng

* Đăng ký tên /mật khẩu.

> Thực ra đây cũng là kiểm soát quyền truy nhập, nhưng không phải truy nhập ở mức thông tin mà ở mức hệ thống. Đây là phương pháp bảo vệ phổ biến nhất vì nó đơn giản ít phí tổn và cũng rất hiệu quả.
> Về lý thuyết nếu mọi người đều giữ kín được mật khẩu và tên đăng ký của mình thì sẽ không xảy ra các truy nhập trái phép. Song điều đó khó đảm bảo trong thực tế vì nhiều nguyên nhân rất đỗi thường làm giảm hiệu quả của lớp bảo vệ này.

**PAGE 32**  
Các mức bảo vệ trên mạng

**PAGE 33**  
Các mức bảo vệ trên mạng
Bảo vệ vật lý
Ngăn cản các truy nhập vật lý vào hệ thống. Thường dùng các biện pháp truyền thống như ngăn cấm tuyệt đối người không phận sự vào phòng đặt máy mạng, dùng ổ khóa trên máy tính hoặc các máy trạm không có ổ mềm.
Tường lửa
Ngăn chặn thâm nhập trái phép và lọc bỏ các gói tin không muốn gửi hoặc nhận vì các lý do nào đó để bảo vệ một máy tính hoặc cả mạng nội bộ

**PAGE 34**  
Các mức bảo vệ trên mạng

* Quản trị mạng

> Công tác quản trị mạng máy tính phải được thực hiện một cách khoa học đảm bảo các yêu cầu sau:

* Toàn bộ hệ thống hoạt động bình thường trong giờ làm việc.
* Có hệ thống dự phòng khi có sự cố về phần cứng hoặc phần mềm xảy ra. Backup dữ liệu quan trọng theo định kỳ.
* Bảo dưỡng mạng theo định kỳ.
* Bảo mật dữ liệu, phân quyền truy cập, tổ chức nhóm làm việc trên mạng

**PAGE 35**  
THÔNG TIN

**PAGE 36**  
Thông tin là những tính chất xác định của vật chất mà con người (hoặc hệ thống kỹ thuật) nhận được từ thế giới vật chất bên ngoài hoặc từ những quá trình xảy ra trong bản thân nó.
Thông tin tồn tại một cách khách quan, không phụ thuộc vào hệ thu cảm

**PAGE 37**  
Tài nguyên thông tin:

* Phần cứng
* Phần mềm
* Dữ liệu
* Môi trường truyền thông giữa các máy tính
* Môi trường làm việc
* Con người

**PAGE 38**  
Các mối đe dọa đối với một hệ thống thông tin và các biện pháp ngăn chặn

**PAGE 39**  
Các mối đe dọa đối với hệ thống thông tin

**PAGE 40**  
Các thành phần chính của ATT

**PAGE 41**  
An toàn vật lý

* An toàn ở mức vật lý là sự bảo vệ tài sản và thông tin của khối sự truy cập vật lý không hợp lệ.
* Đảm bảo an toàn mức vật lý tương đối dễ thực hiện.
* Biện pháp bảo vệ đầu tiên là làm sao cho vị trí của tổ chức càng ít trở thành mục tiêu tấn công càng tốt.

**PAGE 42**  
An toàn vật lý

* Biện pháp bảo vệ thứ hai phát hiện và ngăn chặn các kẻ đột nhập hay kẻ trộm: camera, thiết bị chống trộm.
* Biện pháp bảo vệ thứ ba là khôi phục những dữ liệu hay hệ thống cực kỳ quan trọng bị trộm hay mất mát.

**PAGE 43**  
Thao tác an toàn liên quan những gì mà một tổ chức cần thực hiện để đảm bảo một chính sách an toàn
Thao tác này bao gồm cả hệ thống máy tính, mạng, hệ thống giao tiếp và quản lý thông tin.
Do đó thao tác an toàn bao hàm một lĩnh vực rộng lớn và vì bạn là một chuyên gia an toàn nên bạn phải quan tâm trực tiếp đến các lĩnh vực này

**PAGE 44**  
Quy trình thao tác an toàn
Kiểm soát truy cập
Chứng thực
An toàn mạng sau khi việc thiết lập mạng
Các thao tác an toàn trên đây không liên quan đến việc bảo vệ ở mức vật lý và mức thiết kế

**PAGE 45**  
Quy trình thao tác an toàn

* Sự kết hợp của tất cả các quá trình, các chức năng và các chính sách bao gồm cả yếu tố con người và yếu tố kỹ thuật.
* Yếu tố con người tập trung vào các chính sách được thực thi trong tổ chức.
* Yếu tố kỹ thuật bao gồm các công cụ mà cái đặt vào hệ thống.

**PAGE 46**  
Phần mềm chống virus
Virus máy tính là một vấn đề phiền toái nhất.
Các phương thức chống virus mới ra đời cũng nhanh tương tự như sự xuất hiện của chúng.
File chống virus được cập nhật mỗi hai tuần một lần hay lâu hơn. Nếu các file này cập nhật thường xuyên thì hệ thống có thể là tương đối an toàn.
Phát hiện và diệt virus trực tuyến

**PAGE 47**  
Kiểm soát truy cập bắt buộc
Kiểm soát truy cập tự do
Kiểm soát truy cập theo vai trò

**PAGE 48**  
Kiểm soát truy cập bắt buộc
(MAC - Mandatory Access Control)
Cách truy cập tính, sử dụng một tập các quyền truy cập được định nghĩa trước đối với các file trong hệ thống.
DAC - Discretionary Access Control
Do chủ tài nguyên cấp quyền thiết lập một danh sách kiểm soát truy cập (ACL - Access Control List)

**PAGE 49**  
Kiểm soát truy cập theo vai trò (chức vụ) (RBAC - Role Based Access Control): Truy cập với quyền hạn được xác định trước trong hệ thống, quyền hạn này căn cứ trên chức vụ của người dùng trong tổ chức.

**PAGE 50**  
Chứng thực
Chứng minh "Tôi chính là tôi chứ không phải ai khác" là một phần quan trọng trong ĐỊNH DANH và CHỨNG THỰC.
Ba yếu tố của chứng thực:

* Cái bạn biết (Something you know) - Mật mã hay số PIN
* Cái bạn có (Something you have) - Một card thông minh hay một thiết bị chứng thực.
* Cái bạn sở hữu (Something you are) - Dấu vân tay hay võng mạc mắt của bạn

**PAGE 51**  
Chứng thực bằng sinh trắc học

* Nhận dạng cá nhân bằng các đặc điểm riêng biệt của từng cá thể.
* Hệ thống sinh trắc học gồm các thiết bị quét tay, quét võng mạc mắt, và sắp tới sẽ có thiết bị quét DNA.
* Để có thể truy cập vào tài nguyên thì bạn phải trải qua quá trình nhận dạng vật lý.

**PAGE 52**  
Kế hoạch khôi phục sau biến cố

* Một trong những vấn đề nhức đầu nhất mà các chuyên gia CNTT phải đối mặt.
* Tốn rất nhiều tiền để thực hiện việc kiểm tra, sao lưu, thiết lập hệ thống dự phòng để giữ cho hệ thống hoạt động liên tục.
* Hầu hết các công ty lớn đều đầu tư một số tiền lớn vào kế hoạch khôi phục bao gồm việc sao lưu dữ liệu hay những lập "điểm nóng".
* "Điểm nóng" là một nơi được thiết kế để cung cấp các dịch vụ nhanh chóng và thuận tiện nhất khi có sự cố xảy ra như hệ thống hay mạng bị sập.

**PAGE 53**  
Sơ lược về lịch sử mật mã học

**PAGE 54**  
Sơ lược về lịch sử mật mã học

**PAGE 55**  
Sơ lược về lịch sử mật mã học

**PAGE 56**  
Vai trò của mật mã trong việc bảo mật thông tin

* Mật mã hay mã hóa dữ liệu (cryptography), là một công cụ cơ bản thiết yếu của bảo mật thông tin.
* Mật mã đáp ứng được các nhu cầu về:

> Tính bảo mật (confidentiality)
> Tính chứng thực (authentication)
> Tính không từ chối (non-repudiation) của một hệ truyền tin

**PAGE 57**  
Phân loại các thuật toán mật mã

* Các thuật toán mã hóa khóa bí mật (hệ mã mật khóa bí mật hay khóa đối xứng SKC)
* Các thuật toán mã hóa khóa công khai (các hệ mã khóa công khai PKC).
* Các hệ mã khóa bất đối xứng (AKC).
* Các thuật toán tạo chữ ký số (DSA).
* Các hàm băm (Hash functions).

# Chương 2: CÁC HỆ MÃ ĐỐI XỨNG

#### **Một số khái niệm**

* **Bản rõ – PlainText (X)** được gọi là văn bản gốc. Bản rõ có thể được chia nhỏ có kích thước phù hợp.
* **Bản mã – CipherText (Y)** là bản tin gốc đã được mã hoá.
* **Mã** là thuật toán (E) chuyển bản rõ thành bản mã.
* **Khoá (K)** là thông tin tham số dùng để mã hoá, chỉ có người gửi và người nhận biết. Khoá là độc lập với bản rõ và có độ dài phù hợp với yêu cầu bảo mật.
* **Mã hoá** là quá trình chuyển bản rõ thành bản mã, thông thường bao gồm việc áp dụng thuật toán mã hóa và một số quá trình xử lý thông tin kèm theo.
* **Giải mã** chuyển bản mã thành bản rõ, đây là quá trình ngược lại của mã hóa.
* **Mật mã học** là chuyên ngành khoa học của Khoa học máy tính nghiên cứu về các nguyên lý và phương pháp mã hoá. Hiện nay người ta đưa ra nhiều chuẩn an toàn cho các lĩnh vực khác nhau của công nghệ thông tin.
* **Thám mã** nghiên cứu các nguyên lý và phương pháp giải mã thường là không biết khóa. Thông thường khi đưa các mã mạnh ra làm chuẩn phổ biến công khai các mã đó được các kẻ thám mã cũng như những người phát triển mã tìm hiểu nghiên cứu.
* **Lý thuyết mã** bao gồm cả mật mã và thám mã để đánh giá một mã mạnh hay không.

#### **Giải thuật mật mã hóa**

* **Các hệ mật mã hóa**:
  * **Kiểu của các thao tác được dùng để biến đổi bản rõ thành bản mật**: tất cả các giải thuật mã hóa đều dựa trên 2 nguyên lý:
    * **Thay thế (substitution)**: mỗi thành phần trong bản rõ được ánh xạ đến thành phần khác.
    * **Chuyển vị (transposition)**: các thành phần trong bản rõ được sắp xếp lại.
  * **Yêu cầu cơ bản**: thông tin không bị mất. Phần lớn các hệ mã kết hợp cả 2 nguyên lý qua nhiều bước.
  * **Số khóa được sử dụng**:
    * **1 Khóa**: người gửi và người nhận sử dụng chung khóa.
    * **2 Khóa**: Khóa bí mật/Khóa công khai (mã hóa dùng 1 khóa và giải mã dùng 1 khóa khác).

#### **Mô hình mã đối xứng**

#### **Các hệ mã khóa bí mật**

Các hệ mã khóa bí mật bao gồm:

* Các hệ mật mã cổ điển.
* Các hệ mật hiện đại (mã hóa khối).

#### **Hệ mật mã cổ điển**

* **Kỹ thuật thay thế**:
  * Mật mã Ceasar.
  * Mật mã Playfair.
  * Mật mã Hill.
  * Mật mã Vigenère.
* **Kỹ thuật hoán vị**:
  * Mật mã rail fence.
  * Kỹ thuật hoán vị nâng cao.

##### **Mật mã Ceasar**

* **Lịch sử**: Thế kỷ thứ 3 trước công nguyên, nhà quân sự La Mã Julius Ceasar đưa ra phương pháp mã hóa một bản tin.
* **Nguyên tắc**: Thay thế mỗi chữ trong bản tin bằng chữ đứng sau nó k vị trí trong bảng chữ cái.
  * Ví dụ: Giả sử chọn **k = 3**, ta có bảng chuyển đổi như sau:
    * Chữ ban đầu: a b c d e f g h i j k l m n o p q r s t u v w x y z
    * Chữ thay thế: d e f g h i j k l m n o p q r s t u v w x y z a b c
* **Công thức toán học**: Nếu ta gán số thứ tự cho mỗi chữ trong bảng chữ cái (a=0, b=1, ..., z=25).
  * **Mã hóa**: **c = E(p) = (p + k) mod 26**.
  * **Giải mã**: **p = D(c) = (c – k) mod 26**.
  * Trong đó: p, c là số thứ tự của ký tự trong bảng chữ cái; k là khoá của mã Ceasar; E() hàm mã hóa, D() hàm giải mã.
* **Số lượng khóa**: Có 26 giá trị khác nhau của k, nên có 26 khoá khác nhau. Thực tế độ dài khoá ở đây chỉ là 1, vì mọi ký tự đều tịnh tiến đi một khoảng như nhau.
* **Ví dụ giải mã**: Với k=3, "PHHW PH DIWHU WKH WRJD SDUWB" được giải mã thành "MEET ME AFTER THE TOGA PARTY".
* **Tính an toàn**: Ngày nay phương pháp mã hóa của Ceasar không được xem là an toàn. Đối thủ có thể thử tất cả 25 trường hợp của k rất nhanh chóng. Phương pháp tấn công này được gọi là **phương pháp vét cạn khóa (brute-force attack)**.

##### **Mã Playfair**

* **Đặc điểm**: Mật mã đa ký tự (mỗi lần mã hóa 2 ký tự liên tiếp nhau).
* **Giải thuật**: Dựa trên một **ma trận các chữ cái 5×5** được xây dựng từ một khóa (chuỗi các ký tự).
* **Xây dựng ma trận khóa**:
  * Lần lượt thêm từng ký tự của khóa vào ma trận.
  * Nếu ma trận chưa đầy, thêm các ký tự còn lại trong bảng chữ cái vào ma trận theo thứ tự A - Z.
  * I và J xem như 1 ký tự.
  * Các ký tự trong ma trận không được trùng nhau.
  * Ví dụ: với từ khóa “playfair example” ma trận khóa là:

        ```
        P L A Y F
        I R E X M
        B C D G H
        K N O Q S
        T U V W Z
        ```

* **Giải thuật mật mã hóa**:
  * Mã hóa từng cặp “2 ký tự” liên tiếp nhau.
  * Nếu 2 ký tự này giống nhau thì thêm một ký tự ‘x’ hoặc ‘z’ vào giữa. Ví dụ: balloon tách thành ba lx lo on (vì ll -> lx l).
  * Nếu dư 1 ký tự thì thêm vào ký tự ‘q’ vào cuối. Ví dụ: hat => ha tq.
  * **Quy tắc mã hóa từng cặp**:
    * **Cùng một hàng**: thay bằng hai ký tự tiếp theo trong hàng. Nếu đến cuối hàng thì quay về đầu hàng. Ví dụ: cặp AR được mã hóa thành RM (với khóa MORNACHY).
    * **Cùng một cột**: thay bằng hai ký tự tiếp theo trong cột. Nếu đến cuối cột thì quay về đầu cột. Ví dụ: cặp OV được mã hóa thành HO (với khóa MORNACHY).
    * **Các trường hợp còn lại**: hai ký tự được mã hóa sẽ tạo thành đường chéo của một hình chữ nhật và được thay bằng 2 ký tự trên đường chéo kia. Ví dụ: HS trở thành BP; EA trở thành IM (hoặc JM).
* **Tính an toàn**: Người ta tin rằng mã hóa Playfair không thể bị phá và được quân đội Anh sử dụng trong chiến tranh thế giới lần thứ nhất.
* **Giải thuật giải mã playfair**:
  * Giải mã từng cặp “2 ký tự” liên tiếp nhau.
  * Không thêm hoặc bớt ký tự.
  * **Quy tắc giải mã từng cặp**:
    * **Cùng một hàng**: thay bằng hai ký tự ở trước trong hàng. Nếu ở đầu hàng thì quay về cuối hàng. Ví dụ: cặp RM được giải mã thành AR.
    * **Cùng một cột**: thay bằng hai ký tự ở trên trong cột. Nếu đến đầu cột thì quay về cuối cột. Ví dụ: cặp NW được mã hóa thành WQ.
    * **Các trường hợp còn lại**: hai ký tự được giải mã sẽ tạo thành đường chéo của một hình chữ nhật và được thay bằng 2 ký tự trên đường chéo kia. Ví dụ: HS trở thành BP; EA trở thành IM (hoặc JM).

##### **Mật mã Hill**

* **Đặc điểm**: Giải thuật sử dụng **m ký tự liên tiếp của bản rõ** và thay thế m ký tự khác trong bản mã.
* **Nguyên tắc**: Việc thay thế được thực hiện bởi một phương trình tuyến tính trên các ký tự được gán trị (a=0, b=1, c=2…).
  * Với **m=3**:

        ```
        c1   k11 k12 k13   p1
        c2 = k21 k22 k23 . p2 mod 26
        c3   k31 k32 k33   p3
        ```

        Hay **C = K P mod 26**.
  * **Giải mã**: **P = K⁻¹C mod 26**.
* **Tìm ma trận nghịch đảo**: Sử dụng phương pháp tìm ma trận nghịch đảo của đại số tuyến tính. Viết ma trận khóa K và ma trận đơn vị I cạnh nhau, sau đó áp dụng các phép biến đổi tuyến tính lên cả hai ma trận K và I để biến K thành I. Khi đó I sẽ thành K⁻¹.

##### **Mã hóa thay thế đa bảng (Polyalphabetic Substitution Cipher)**

* **Lịch sử**: Với sự phát hiện ra quy luật phân bố tần suất, các nhà phá mã đang tạm thời chiếm ưu thế trong cuộc chiến mã hóa-phá mã. Cho đến thế kỷ thứ 15, một nhà ngoại giao người Pháp tên là **Vigenère** đã tìm ra phương án mã hóa thay thế đa bảng.
* **Nguyên tắc**: Phương pháp Vigenère dựa trên bảng tra cứu mã hóa và giải mã.
* **Thuật toán**:
  * Sao chép, ghép nội dung khóa sao cho chiều dài khóa bằng với chiều dài bản rõ cần mã hóa.
  * Tách từng ký tự trong khóa và từng ký tự trong bản rõ rồi tra cứu trong bảng, giao giữa hàng và cột ta được ký tự đã được mã hóa.
  * Ví dụ: Mã hóa bản tin “We are discovered, save yourself” với Khóa: DECEPTIVE, Bản mã: ZICVT WQNGRZGVT W AVZH CQYGLMGJ.
* **Tính an toàn**: Trong 3 thế kỷ sau đó mã hóa Vigenère được xem là mã hóa không thể bị phá và được biết dưới cái tên “le chipffre indechiffrable” (mật mã không thể phá nổi). Đến thế kỷ 19, nhà khoa học người Anh Charles Barbage, đã tìm ra cách phá mã Vigenère.

##### **Mã hoán vị (Permutation Cipher)**

* **Cách thực hiện đơn giản**: Ghi bản rõ theo từng hàng, sau đó kết xuất bản mã dựa trên các cột.
  * Ví dụ bản rõ “attackpostponeduntilthisnoon” được viết lại thành bảng 4 x 7 như sau:

        ```
        a t t a c k p
        o s t p o n e
        d u n t i l t
        h i s n o o n
        ```

        Sau đó đọc theo cột để tạo bản mã.

#### **Mã hóa khối (Mã hóa hiện đại)**

##### **Quy trình mã hóa theo khối**

* **Data Path**: Thông thường, quy trình mã hóa bao gồm nhiều chu kỳ mã hóa (round) liên tiếp nhau; mỗi chu kỳ gồm nhiều thao tác mã hóa.
* **Key Schedule**: Từ khóa gốc (secret key), phát sinh (có quy luật) các giá trị khóa sẽ được sử dụng trong mỗi chu kỳ mã hóa (round key).

##### **Thuật toán DES (Data Encryption Standard)**

* **Ý tưởng**: mã hóa tích.
  * **Key**: 56 bit.
  * **Block**: 64 bit.
* **Lịch sử**: Được IBM phát triển từ phương pháp Lucifer. Chính thức công bố năm 1975. Được chọn là Chuẩn xử lý thông tin liên bang (Federal Information Processing Standard - FIPS) năm 1976.
* **Tính an toàn**: Về mặt khái niệm DES là thuật toán mở, nghĩa là mọi người đều biết thuật toán này. Tuy nhiên chìa khoá của DES có độ dài tới 56 bit, nghĩa là số lần thử tối đa để tìm được chìa khoá lên đến 2⁵⁶, trung bình là 2⁵⁵ = 36.028.797.018.963.968 lần, một con số rất lớn.
* **Cơ chế**: DES được thực hiện nhờ các phép dịch, hoán vị.
* **Quy trình của thuật toán DES**:
  * DES nhận vào một thông điệp M 64 bit, một khóa K 56 bit và cho ra một bảng mã C 64 bit.
  * **Bước 1**: Áp dụng một phép hoán vị bit khởi tạo **IP (Initial Permutation)** vào M cho ra M’: M’.=.IP(M).
  * **Bước 2**: Chia M’ thành hai phần: nửa trái **L0 = 32 bit** và nửa phải **R0 = 32 bit**.
  * **Bước 3**: Thực hiện các phép toán sau với **i = 1, 2, ... 16 (có 16 vòng)**:
    * **Li = Ri-1**.
    * **Ri = Li-1 ⨁ f(Ri-1, Ki)**.
  * **Bước 4**: Hoán vị với phép hoán vị **IP⁻¹** để được bản mã cuối.
* **Hàm f trong DES**: Bao gồm các bước Expansion, ⨁, S-box (S1-S8), Permutation.
  * **Expansion**: Bảng chọn lựa bit E mở rộng từ 32 bit thành 48 bit.
  * **S-box**: Có 8 S-box (S1 đến S8) dùng để thay thế 6 bit đầu vào bằng 4 bit đầu ra.
  * **Permutation**: Bảng hoán vị P.
* **Key Schedule**:
  * Thực tế, K là một dãy 64 bits trong đó có **56 bits làm khóa** và **8 bits dùng để kiểm tra lỗi** (Kiểm tra chắn lẻ).
  * Các bit nằm ở vị trí 8, 16, 24 ... 64 là các bit dùng để kiểm tra chẵn lẻ.
  * Cho một khóa K 64 bits, bỏ các bit kiểm tra chẵn lẻ sẽ được 56 bits khóa.
  * Cho 56 bit này hoán vị theo bảng hoán vị **PC-1**. Ta có: PC-1(K)=C0D0, trong đó C0 chứa 28 bit bên trái, D0 chứa 28 bit bên phải.
  * **Thao tác xoay vòng bit**: <<<: Xoay vòng sang trái; >>>: Xoay vòng sang phải.
  * Với subkey thứ 1, 2, 9, 16: xoay vòng 1 vị trí.
  * Với subkey còn lại: xoay vòng 2 vị trí.
  * Các hoán vị trong Key Schedule bao gồm PC-1 (chọn 56 bit) và PC-2 (chọn 48 bit).
* **Ưu điểm – Nhược điểm**:
  * **Ưu điểm**:
    * Có tính bảo mật cao.
    * Công khai, dễ hiểu.
    * Nó có thể triển khai trên thiết bị điện tử có kích thước nhỏ.
  * **Nhược điểm**:
    * Khóa yếu là các khóa mà theo thuật toán sinh khóa con thì tất cả 16 khóa con đều như nhau: K1=K2=... =K16.
* **Một số nhận xét**:
  * **4 khóa yếu (weak key)**: Gồm toàn bit 0; Gồm toàn bit 1; Gồm ½ là bit 0 (liên tiếp), ½ là bit 1 (liên tiếp).
  * **12 khóa “tương đối yếu” (semi-weak key)**: Khóa có dạng: 7 bit 0 (liên tiếp), 7 bit 1 (liên tiếp).
* **Giải mã DES**:
  * Thực hiện tương tự như mã hóa, tuy nhiên ở vòng lặp i sẽ sử dụng subkey Ki = K17-i.
  * Vòng lặp 1 sử dụng K16.
  * Vòng lặp 2 sử dụng K15.
  * ... và cứ thế.

##### **Thuật toán 3-DES (TripleDES)**

* **Mục đích**: Khắc phục yếu điểm kích thước khóa ngắn của mã hóa DES.
* **Nguyên tắc**: Sử dụng mã hóa DES nhiều lần với các khóa khác nhau cho cùng một bản tin.
* **Chiều dài khóa**: 168 bit.
* **Công thức**: **C = E(D(E(P, K1), K2), K3)**.

# CHương 3: Hệ mã bất đối xứng

Dưới đây là toàn bộ nội dung của Chương 3: Các hệ mã hóa công khai (mã hóa bất đối xứng) từ các nguồn bạn cung cấp:

### **CHƯƠNG 3 CÁC HỆ MÃ HÓA CÔNG KHAI (MÃ HÓA BẤT ĐỐI XỨNG)**

**Giới thiệu**

* **Nguồn gốc**: Hệ mật mã khóa đối xứng (cổ điển và hiện đại) không đáp ứng được hai mục tiêu an toàn là **xác thực** và **chống phủ nhận**.
* Quản lý khóa đối xứng là một vấn đề nan giải.
* Cần tìm một phương pháp mã hóa khác có thể giải quyết được các vấn đề của mã hóa đối xứng.
* Whitfield Diffie và Martin Hellman đã tìm ra một phương pháp mã hóa khóa công khai.

**Các khái niệm và sơ đồ**

* **Sơ đồ mã hóa bất đối xứng**, còn được gọi là **mã hóa khóa công khai (Public Key Cryptography – PKC)**, sử dụng một cặp khóa cho quá trình mã hóa và giải mã.
* Cặp khóa này phải đảm bảo **tính toàn vẹn và xác thực** cho chủ thể của khóa.

**Hệ mật mã khóa công khai**

* Các giải thuật mật mã khóa công khai sử dụng **một khóa để mật mã hóa và một khóa khác có liên quan để giải mật mã**.
* Đặc điểm:
  * Không thể tính lại khóa giải mật mã nếu biết trước giải thuật mật mã hóa và khóa dùng mã hóa.
  * Một trong hai khóa đều có thể dùng để mã hóa và khóa còn lại dùng để giải mật mã.

**Các thành phần giải thuật khóa công khai**
Giải thuật khóa công khai gồm 6 thành phần:

* **Bản rõ (Plaintext)**: Thông điệp có thể đọc được, là đầu vào của giải thuật.
* **Giải thuật mật mã hóa**.
* **Khóa công khai và khóa bí mật**: Một cặp khóa được chọn sao cho một khóa dùng để mật mã hóa và một khóa dùng để giải mật mã.
* **Bản mã (Cipher Text)**: Thông điệp đầu ra ở dạng không đọc được, phụ thuộc vào bản rõ và khóa; nghĩa là với cùng một thông điệp, hai khóa khác nhau sẽ sinh ra hai bản mã khác nhau.

**Các bước thực hiện**

* Mỗi người dùng tạo một cặp khóa để mã hóa và giải mã.
* Mỗi người dùng đăng ký một trong hai khóa làm khóa công khai sao cho mọi người đều có thể truy cập được. Khóa còn lại được giữ bí mật.
* **Ví dụ**: An muốn gửi Bình một thông điệp bí mật. An mã hóa thông điệp bằng khóa công khai của Bình. Khi Bình nhận được thông điệp, Bình sẽ giải mã thông điệp bằng khóa bí mật của mình. Ngoài Bình, không người nào có khả năng giải mã vì chỉ có Bình có khóa để giải mã.

**Sơ đồ mã hóa**

* **Sơ đồ mã hóa bất đối xứng (dùng cho mã hóa)**:
  * `CipherText = E(Kp, Plaintext)`
  * `Plaintext = D(Ks, E(Kp, Plaintext))`
* **Sơ đồ mã hóa bất đối xứng (dùng chữ ký điện tử)**:
  * `SignedM = E(KS, Mhash)`
  * `Mhash = D(KP, E(KS, Mhash))`

**Các yêu cầu**

* Dễ dàng tính được cặp khóa công khai `Kp` và bí mật `Ks`.
* Dễ dàng tính được bản mã với bản rõ và khóa công khai cho trước `C = E(Kp, P)`.
* Dễ dàng tính được bản rõ từ bản mã và khóa bí mật cho trước `P = D(Ks, C) = D(Ks E(Kp, P))`.
* Không thể tính `KS` từ `KP`.
* Không thể tính được bản rõ P từ khóa `KP` và bản mã cho trước.
* Mã hóa và giải mã được thực hiện theo một trong hai quá trình `P = D(KS, E(KP, P)) = D(KP, E(KS, P))`.

**Lý thuyết liên quan: số học đồng dư**

* **Số học đồng dư**:
  * `a mod n`
  * `a op b mod n` với `op = +, −, ∗, /, mũ`
* **Ví dụ**:
  * `40 mod 6 = ?`
  * `5 + 2 mod 6 = ?`
  * `9 − 4 mod 3 = ?`
  * `5 ∗ 3 mod 6 = ?`
  * `4/2 mod 3 = ?`

**Thủ tục bình phương**

* Dựa vào tính chất: `a ∗ b mod n = a mod n ∗ b mod n mod n`.
* **Mô tả thuật toán ModExp1(a, b, s)**:
  * **Đầu vào**: 3 số nguyên dương a, b, s sao cho a < s. b[n − 1] . . . bb là biểu diễn nhị phân của b, n = ⌈log2b⌉.
  * **Đầu ra**: `ab mod s`.
  * **Các bước**:
    * `p = a mod s`
    * `for i = 1 to n − 1`: `p[i] = p[i − 1]^2 mod s`
    * `r = 1`
    * `for i = 0 to n − 1`: `if b[i] = 1 then r = r ∗ p[i] mod s`
    * `return r`
* **Bài tập ví dụ**: Tính `6^73 mod 100`.
  * Với `73 = 1001001_2` (7 bit).
  * Tính các `p[i]`:
    * `p = 6 mod 100 = 6`
    * `p = p^2 mod 100 = 6^2 mod 100 = 36`
    * `p = p^2 mod 100 = 36^2 mod 100 = 96`
    * `p = p^2 mod 100 = 96^2 mod 100 = 16`
    * `p = p^2 mod 100 = 16^2 mod 100 = 56`
    * `p = p^2 mod 100 = 56^2 mod 100 = 36`
  * Có `b, b, b` là 1:
    * `b`: `r = r ∗ p mod 100 = 1 ∗ 6 mod 100 = 6`
    * `b`: `r = r ∗ p mod 100 = 6 ∗ 16 mod 100 = 96`
    * `b`: `r = r ∗ p mod 100 = 96 ∗ 96 mod 100 = 16` (Lưu ý: `p` không được tính trong đoạn văn bản nhưng dựa trên quy luật, đây sẽ là `p^2 mod 100 = 36^2 mod 100 = 1296 mod 100 = 96`. Sau đó `r = 96 * 96 mod 100 = 9216 mod 100 = 16`. Có vẻ có sự nhầm lẫn nhỏ trong chỉ số `b` và `p` trong nguồn, nhưng kết quả cuối cùng là 16).
  * Vậy `6^73 mod 100 = 16`.
* **Các bài tập khác**:
  * Tính `12^78 mod 25`
  * Tính `15^81 mod 50`
  * Tính `8^67 mod 10`
  * Tính `25^67 mod 70`

**Giải thuật Euclide mở rộng**

* **Giải thuật Euclide**: Tìm **USCLN(a, b)** dựa trên tính chất: nếu a > b thì `USCLN(a, b) = USCLN(a mod b, b)`.
* **Giải thuật Euclide mở rộng**: Tính x, y sao cho `a ∗ x + b ∗ y = USCLN(a, b)`.
* Giải quyết bài toán tìm x sao cho `a ∗ x = 1 mod s`.
* **Extended-Euclid (a, b)**:
  * **Đầu vào**: 2 số nguyên dương a, b.
  * **Đầu ra**: 3 số nguyên x, y, d sao cho `d = USCLN(a, b)` và `ax + by = d`.
  * **Các bước**:
        1. Nếu `b = 0` thì trả về `(1, 0, a)`.
        2. Tìm `q, r` sao cho `a = b ∗ q + r`.
        3. `(x’, y’, d) = Extended − Euclid(b, r)`.
        4. Trả về `(y’, x’ − q ∗ y’, d)`.
* **Ví dụ**: Dùng Euclide mở rộng tìm USCLN(120, 23):
  * Quá trình đệ quy và trả về các giá trị x, y, d qua các bước được trình bày chi tiết trong nguồn.
  * **Kết quả cuối cùng**: USCLN(120, 23) = 1. Các hệ số x và y là: **x = -9, y = 47**.
  * Kiểm tra: `120 * (-9) + 23 * 47 = -1080 + 1081 = 1`.
* **Các bài tập ví dụ khác**:
  * Dùng Euclide mở rộng tìm x sao cho `51 ∗ x mod 100 = 1`
  * `80 ∗ x mod 79 = 1`
  * `1013 * x mod 1019 = 1`

**Hệ thống mã hóa RSA**

* Được xây dựng tại học viện MIT năm 1977.
* Đặt theo tên của các tác giả: Ron Rivest, Adi Shamir và Len Adleman.
* Là một hệ mã hóa khối và sử dụng hàm một chiều phân tích một số thành thừa số nguyên tố.
* Để đảm bảo an toàn, khuyến nghị sử dụng khóa **2048 bit hoặc lớn hơn 3072 bit** trong tương lai (khởi đầu là 1024 bit).
* **Mã hóa và giải mã được tính theo công thức**:
  * `C = Pe mod n`
  * `P = Cd mod n`
* **Các yêu cầu**:
  * Có thể tìm được các giá trị e, d, n sao cho `P^(e.d) = P (mod n)` với mọi P < n.
  * Dễ dàng tính được `P^e` và `C^d` với mọi P < n.
  * Không thể tính được d từ e và n.
* **Thuật toán sinh khóa RSA**:
    1. Chọn 2 số nguyên tố lớn `p` và `q`.
    2. Tính `n = p ∗ q`.
    3. Tính `m = φ(n) = (p − 1). (q − 1)`.
    4. Tìm một số `e` sao cho `e` là nguyên tố cùng nhau với `m` → `UCLN(e, m) = 1`.
    5. Tìm một số `d` sao cho `(e ∗ d) mod m = 1`.
    6. **Kết quả**: khóa công khai `PK = {e, n}`, khóa bí mật `SK = {d, n}`.
* **Thuật toán brute-force để tìm d (d nhỏ)**:
  * `Function Compute_d(e, phi_n)`:
    * `for i trong khoảng (1, 1000) do`
      * `x ← i ∗ phi_n + 1 / e`
      * `y ← (e ∗ x) % phi_n`
      * `if y = 1 return x`
* **Ví dụ**: Cho hệ mã RSA có `p = 11, q = 47` và `e = 3`.
  * **Tìm khóa công khai và khóa bí mật**:
        1. `p = 11, q = 47`.
        2. `n = p ∗ q = 517`.
        3. `m = φ(n) = (11 − 1). (47 − 1) = 460`.
        4. `1 < e < 460` và `(3, 460)` là nguyên tố cùng nhau.
        5. Dùng brute force: `d = 307`.
    * **Khóa công khai**: `PK = (e, n) = (3, 517)`.
    * **Khóa bí mật**: `SK = (d, n) = (307, 517)`.
  * **Mã hóa P = 26**: `C = P^e mod n = 26^3 mod 517 = 515`.
* **Các bài tập ví dụ khác**:
  * Cho `p = 7, q = 19, e = 5`. Tìm khóa công khai, bí mật, và mã hóa `P = 6`.
  * Cho `p = 17, q = 23, e = 7`. Tìm khóa công khai, bí mật, và mã hóa `P = 50`.
  * Cho `p = 61, q = 53`. Tìm khóa công khai, bí mật, và mã hóa `P = 123`.
  * Cho `p = 43, q = 59`. Tìm khóa công khai, bí mật, và mã hóa `P = 150`.
  * Cho `p = 7, q = 11`. An dùng khóa công khai `Pk = (17, 77)`. Tìm khóa bí mật. Biết ký tự A-Z biểu diễn bằng số 0-25, dấu cách là 26. Bảo gửi An tin "HELLO WORD". Hỏi bản mã tương ứng là gì?.
* Để tiện cho việc giao dịch trên mạng có sử dụng truyền tin mật, người ta lưu trữ các khóa công khai của các người dùng tại một điểm công cộng.
* **Độ an toàn của RSA dựa vào độ phức tạp của bài toán phân tích một số nguyên dương cho trước n thành hai thừa số nguyên tố p và q**.
* **Lựa chọn p, q**:
  * Đảm bảo rằng bài toán phân tích thừa số nguyên tố `PTTSNT(n)` thật sự khó.
  * Tránh tình trạng p, q rơi vào những trường hợp đặc biệt (ví dụ: p - 1 có các thừa số nguyên tố nhỏ).
  * p, q phải có độ dài tối thiểu 512 bit và xấp xỉ nhau.
* **Lựa chọn e**:
  * e nhỏ nhất có thể.
  * e không quá nhỏ để tránh bị tấn công theo dạng “low exponent”.
* **Lựa chọn d**:
  * d không quá nhỏ (`d < sqrt(n)/4`) để tránh tấn công dạng “low decryption”.

**Hệ mã hóa Elgamal**

* Được T. ElGamal giới thiệu vào năm 1984 dựa trên cơ sở ý tưởng từ Diffie-Hellman.
* Được sử dụng trong việc mã hóa dữ liệu, chữ ký số, trao đổi khóa.
* **Tính an toàn dựa trên tính khó giải của bài toán Logarit rời rạc**.
* **Thuật toán sinh khóa (bên nhận và bên gửi)**:
  * Chọn một số nguyên tố lớn `p` (thường có độ dài từ 1024 đến 2048 bit) và hai số nguyên ngẫu nhiên `ε` và `a`, cả hai đều nhỏ hơn p.
  * Tính `y = ε^a (mod p)`.
  * **Khóa công khai** được lấy là `(p, ε, y)`.
  * **Khóa bí mật** là `a`.
* **Thuật toán sinh mã (bên gửi)**:
  * Chọn giá trị `k (k < p)` và tính toán khóa `K = y^k mod p`.
  * Tính cặp mã, trong đó P là bản rõ:
    * `C1 = ε^k mod p`
    * `C2 = K.P mod p`
  * Cặp `(C1, C2)` được gửi đi, đồng thời `k` bị hủy đi.
* **Thuật toán giải mã (bên nhận)**:
  * Nhận được cặp mã `(C1, C2)` thực hiện các bước Khôi phục bản rõ:
    * `P = C2 / C1^a mod p`
    * Với `C1^(-a) mod p = C1^(p-a-1) mod p`.
* **Ví dụ**: Trước khi bắt đầu truyền tin, An chọn `p = 97`, chọn ngẫu nhiên `ε = 5, a = 58`. Bình muốn gửi cho An một tài liệu mật `P = 3`, Bình chọn ngẫu nhiên `k = 36`.
* **Ưu điểm**:
  * Độ an toàn của mã hóa bất đối xứng cao.
  * Cung cấp được tính chứng thực, toàn vẹn dữ liệu.
  * Thuận tiện phân phối khóa.
* **Hạn chế**:
  * Xử lý chậm hơn so với mã hóa đối xứng.
  * Gặp khó khăn nếu mất khóa bí mật.
  * Phức tạp trong vấn đề tìm số nguyên tố và ngẫu nhiên.
