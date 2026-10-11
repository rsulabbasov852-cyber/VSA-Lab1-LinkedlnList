# Singly Linked List və Doubly Linked List müqayisəsi

## 1. Struktur fərqləri
**Singly Linked List:** hər düyündə `data` və yalnız `next` göstəricisi var. Siyahı bir istiqamətdə gedir: `10 -> 20 -> 30 -> None`.

**Doubly Linked List:** hər düyündə `data`, `next` və `prev` göstəriciləri var. Siyahı iki istiqamətdə gedir: `None <-> 10 <-> 20 <-> 30 <-> None`.

## 2. Üstünlüklər
| Singly | Doubly |
|---|---|
| Quruluşu sadədir, reallaşdırması asandır | Həm irəli, həm geri hərəkət etmək olur |
| Hər düyündə az yaddaş işlədir | Düyünü silmək üçün əvvəlki düyünü axtarmaq lazım deyil (`prev` var) |
| Əvvələ əlavə və silmə O(1) | Həm əvvəldən, həm sondan (tail varsa) əməliyyat O(1) |

## 3. Çatışmazlıqlar
| Singly | Doubly |
|---|---|
| Geriyə getmək mümkün deyil | Hər düyündə əlavə göstərici saxlanılır |
| Verilmiş düyünü silmək üçün əvvəlki düyünü tapmaq lazımdır (O(n)) | Əlavə/silmədə iki göstərici yenilənməlidir, səhv ehtimalı artır |
| Sondan əməliyyat üçün bütün siyahını gəzmək lazımdır | Kod daha mürəkkəbdir |

## 4. Yaddaş sərfi
Singly Linked List-də düyün başına 1 göstərici, Doubly Linked List-də 2 göstərici saxlanılır. Məsələn, 64-bit sistemdə hər göstərici 8 bayt olduqda, Doubly Linked List hər düyün üçün təxminən 8 bayt çox yaddaş tələb edir. Böyük siyahılarda bu fərq nəzərə çarpır.

## 5. İrəli və geri traversing
- **Singly:** yalnız `head`-dən `None`-a doğru (irəli) gəzmək olur.
- **Doubly:** `head`-dən `tail`-ə (`next` ilə) və `tail`-dən `head`-ə (`prev` ilə) gəzmək olur.

## Nəticə
Yaddaş məhduddursa və yalnız irəli gəzmək kifayətdirsə, Singly Linked List daha münasibdir. Geriyə hərəkət və düyünün tez silinməsi lazım olan hallarda (məsələn, brauzer tarixçəsi, undo/redo) Doubly Linked List üstündür.
