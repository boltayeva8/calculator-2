# 🔢 Calculator (Kalkulyator)

Arifmetik amallarni bajaruvchi konsol ilovasi — Python dasturlash tilida yozilgan.

## 📌 Loyiha haqida

Bu loyiha **11-sinf Informatika** fanidan tayyorlangan. Dastur foydalanuvchidan ikki son va amal turini qabul qilib, natijani hisoblaydi. Kod funksiyalar asosida tuzilgan, input validatsiyasi va xatoliklarni boshqarish (error handling) to'liq amalga oshirilgan.

## ⚙️ Imkoniyatlar

| # | Amal | Tavsif |
|---|------|--------|
| 1 | Qo'shish (`+`) | Ikki sonni qo'shish |
| 2 | Ayirish (`-`) | Ikki sonni ayirish |
| 3 | Ko'paytirish (`*`) | Ikki sonni ko'paytirish |
| 4 | Bo'lish (`/`) | Ikki sonni bo'lish |
| 5 | Darajaga ko'tarish (`**`) | a ni b-darajaga ko'tarish |
| 6 | Qoldiqli bo'lish (`%`) | Bo'lishdan qoldiqni hisoblash |
| 7 | Butun bo'lish (`//`) | Butun qismini hisoblash |

## 🛡️ Error Handling

- **Noto'g'ri input** — son o'rniga matn kiritilsa, qayta so'raydi (`ValueError`)
- **Nolga bo'lish** — 0 ga bo'lishda xato xabari chiqaradi (`ZeroDivisionError`)
- **Haddan tashqari katta son** — natija juda katta bo'lsa aniqlaydi (`OverflowError`)
- **Kutilmagan xatoliklar** — barcha boshqa xatoliklarni ushlaydi (`Exception`)

## 🏗️ Kod strukturasi

```
calculator.py
│
├── qoshish(a, b)            # Qo'shish funksiyasi
├── ayirish(a, b)            # Ayirish funksiyasi
├── kopaytirish(a, b)        # Ko'paytirish funksiyasi
├── bolish(a, b)             # Bo'lish funksiyasi (nolga himoya)
├── darajaga_ko_tarish(a, b) # Darajaga ko'tarish
├── qoldiqli_bolish(a, b)    # Qoldiqli bo'lish (nolga himoya)
├── butun_bolish(a, b)       # Butun bo'lish (nolga himoya)
│
├── AMALLAR                  # Amallar lug'ati (dict)
│
├── menyu_korsatish()        # Menyu chiqarish
├── son_olish(xabar)         # Input validatsiyasi
├── natijani_chiqarish()     # Natijani formatlash
│
└── asosiy()                 # Dasturning asosiy sikli
```

## 🚀 Ishga tushirish

```bash
python calculator.py
```

## 📸 Namuna

```
🎯 Kalkulyator dasturiga xush kelibsiz!
   Arifmetik amallarni tanlang va hisoblang.

         KALKULYATOR
  1. Qo'shish (+)
  2. Ayirish (-)
  3. Ko'paytirish (*)
  4. Bo'lish (/)
  5. Darajaga ko'tarish (^)
  6. Qoldiqli bo'lish (%)
  7. Butun bo'lish (//)
  0. Chiqish

  Amalni tanlang (0-7): 1

  📌 Tanlangan amal: Qo'shish (+)
  1-son kiriting: 25
  2-son kiriting: 17

  ✅ Qo'shish (+): 25 va 17 => Natija: 42
```

## 🧰 Texnologiyalar

- **Til:** Python 3
- **Paradigma:** Funksional dasturlash
- **Kutubxonalar:** Standart kutubxona (qo'shimcha o'rnatish talab qilinmaydi)

## 👨‍💻 Muallif

11-sinf o'quvchisi — Informatika fanidan loyiha ishi
