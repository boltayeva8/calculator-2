"""
Kalkulyator — Arifmetik amallarni bajaruvchi konsol ilovasi.
Funksiyalar yordamida tuzilgan, xatoliklarni 
boshqarish (error handling) mavjud.
"""
def qoshish(a, b):
    """Ikki sonni qo'shish."""
    return a + b

def ayirish(a, b):
    """Ikki sonni ayirish."""
    return a - b

def kopaytirish(a, b):
    """Ikki sonni ko'paytirish."""
    return a * b
def bolish(a, b):
    """Ikki sonni bo'lish. Nolga bo'lishdan himoya qilingan."""
    if b == 0:
        raise ZeroDivisionError("Xatolik: Sonni 0 ga bo'lish mumkin emas!")
    return a / b
def darajaga_ko_tarish(a, b):
    """a sonini b darajaga ko'tarish."""
    return a ** b

def qoldiqli_bolish(a, b):
    """Ikki sonni qoldiqli bo'lish. Nolga bo'lishdan himoya qilingan."""
    if b == 0:
        raise ZeroDivisionError("Xatolik: Sonni 0 ga bo'lish mumkin emas!")
    return a % b

def butun_bolish(a, b):
    """Ikki sonni butun bo'lish (//). Nolga bo'lishdan himoya qilingan."""
    if b == 0:
        raise ZeroDivisionError("Xatolik: Sonni 0 ga bo'lish mumkin emas!")
    return a // b


# ==================== Amallar ro'yxati ====================

AMALLAR = {
    "1": ("Qo'shish (+)",         qoshish),
    "2": ("Ayirish (-)",          ayirish),
    "3": ("Ko'paytirish (*)",     kopaytirish),
    "4": ("Bo'lish (/)",          bolish),
    "5": ("Darajaga ko'tarish (^)", darajaga_ko_tarish),
    "6": ("Qoldiqli bo'lish (%)", qoldiqli_bolish),
    "7": ("Butun bo'lish (//)",   butun_bolish),
}


# ==================== Yordamchi funksiyalar ====================

def menyu_korsatish():
    """Foydalanuvchiga menyuni chiqarish."""
    print("         KALKULYATOR  ")
    for kalit, (nomi, _) in AMALLAR.items():
        print(f"  {kalit}. {nomi}")
    print("  0. Chiqish")



def son_olish(xabar):
    """
    Foydalanuvchidan son kiritishni so'raydi.
    Noto'g'ri kiritilgan qiymatni qayta so'raydi.
    """
    while True:
        kiritma = input(xabar)
        try:
            son = float(kiritma)
            return son
        except ValueError:
            print(f"  ⚠ '{kiritma}' — bu son emas. Iltimos, to'g'ri son kiriting.")


def natijani_chiqarish(amal_nomi, a, b, natija):
    """Natijani chiroyli formatda chiqarish."""
    # Agar natija butun son bo'lsa, kasr qismini olib tashlash
    if isinstance(natija, float) and natija == int(natija):
        natija = int(natija)

    # Kiritilgan sonlarni ham tozalash
    a_chop = int(a) if a == int(a) else a
    b_chop = int(b) if b == int(b) else b

    print(f"\n  ✅ {amal_nomi}: {a_chop} va {b_chop} => Natija: {natija}")


# ==================== Asosiy dastur ====================

def asosiy():
    """Kalkulyatorning asosiy sikli."""
    print("\n🎯 Kalkulyator dasturiga xush kelibsiz!")
    print("   Arifmetik amallarni tanlang va hisoblang.\n")

    while True:
        menyu_korsatish()

        tanlov = input("\n  Amalni tanlang (0-7): ").strip()

        # Chiqish
        if tanlov == "0":
            print("\n👋 Dasturdan chiqildi. Xayr!")
            break

        # Noto'g'ri tanlov
        if tanlov not in AMALLAR:
            print("\n  ⚠ Noto'g'ri tanlov! Iltimos, 0 dan 7 gacha raqam kiriting.")
            continue

        amal_nomi, funksiya = AMALLAR[tanlov]

        print(f"\n  📌 Tanlangan amal: {amal_nomi}")

        # Sonlarni kiritish
        birinchi_son = son_olish("  1-son kiriting: ")
        ikkinchi_son = son_olish("  2-son kiriting: ")

        # Amalni bajarish (xatoliklarni ushlash bilan)
        try:
            natija = funksiya(birinchi_son, ikkinchi_son)
            natijani_chiqarish(amal_nomi, birinchi_son, ikkinchi_son, natija)
        except ZeroDivisionError as xato:
            print(f"\n  ❌ {xato}")
        except OverflowError:
            print("\n  ❌ Xatolik: Natija juda katta, hisoblash imkonsiz!")
        except Exception as xato:
            print(f"\n  ❌ Kutilmagan xatolik: {xato}")

        # Davom etish yoki yo'qligini so'rash
        davom = input("\n  Yana hisoblashni xohlaysizmi? (ha/yo'q): ").strip().lower()
        if davom in ("yo'q", "yoq", "y", "n", "no"):
            print("\n👋 Dasturdan chiqildi. Xayr!")
            break


# Dasturni ishga tushirish
if __name__ == "__main__":
    asosiy()
