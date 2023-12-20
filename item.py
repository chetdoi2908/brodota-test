import pyautogui
import time
import button


class ItemInfo:
    def __init__(self, para_name, para_item_number=0):
        self.name = para_name
        self.img = "data\\image\\item\\" + para_name + ".png"
        self.number = para_item_number

    def reset_item_number(self):
        self.number = 0


ShopDiscount = ItemInfo("ShopDiscount")

Investment_lv1_precise = ItemInfo("Investment_lv1_precise")
TomeOfKnowledge = ItemInfo("TomeOfKnowledge")
Exp20_Range5 = ItemInfo("Exp20_Range5")

Exp40_Luck6 = ItemInfo("Exp40_Luck6")

Locomotive = ItemInfo("Locomotive")

MasterChefHat = ItemInfo("MasterChefHat")

Helmet_32Luck_Precise = ItemInfo("Helmet_32Luck_Precise")

# WitlessShako_Health_Precise
WitlessShako_Health_Precise = ItemInfo("WitlessShako_Health_Precise")

# NorthWind_Luck13
NorthWind_Luck13 = ItemInfo("NorthWind_Luck13")

# Vtuber_Inves198_Speed7
Vtuber_Inves198_Speed7 = ItemInfo("Vtuber_Inves198_Speed7")

# Bicycle_lv3
Bicycle_lv3 = ItemInfo("Bicycle_lv3")
Attack16_Arcane16 = ItemInfo("Attack16_Arcane16")
Attack16_Strike16 = ItemInfo("Attack16_Strike16")
Critical30_Defense10 = ItemInfo("Critical30_Defense10")
HealthRegen12_HitRecovery15 = ItemInfo("HealthRegen12_HitRecovery15")
Holding_30HealthRegen = ItemInfo("Holding_30HealthRegen")
Luck60_Speed25 = ItemInfo("Luck60_Speed25")
SplitTheVoid = ItemInfo("SplitTheVoid")


def buy_item(ItemInfo):
    """
    This function is used to buy a specific item.

    Parameters:
    ItemInfo (ItemInfo object): The information of the item to buy.

    Returns:
    True if the item is bought successfully, False otherwise.
    """
    try:
        res = pyautogui.locateOnScreen(
            ItemInfo.img, confidence=0.8, region=(0, 0, 1916, 1134))
        print("xuat hien ", ItemInfo.name)
        res_center = pyautogui.center(res)
        pyautogui.moveTo(res_center)
        pyautogui.click(res_center)
        return True
    except pyautogui.ImageNotFoundException:
        return False


def buy_item_info(ItemInfo, number_item=1):
    """
    This function is used to buy a specific number of a specific item.

    Parameters:
    ItemInfo (ItemInfo object): The information of the item to buy.
    number_item (int): The number of items to buy.

    Returns:
    Nothing.
    """
    number = ItemInfo.number
    if number_item > number:
        number_buy = number_item - number
        for n in range(0, number_buy):
            buy = buy_item(ItemInfo)
            if buy is True:
                print("Bạn đã có {} cái {}".format(
                    ItemInfo.number, ItemInfo.name))
                print("Bạn cần mua thêm {} cái {} nữa".format(
                    number_buy, ItemInfo.name))
                if button.check_not_money():
                    break
                else:
                    number = number + 1
                    print("Bạn đã mua thành công 1 cái {}, bạn cần mua thêm {} nữa".format(
                        ItemInfo.name, number_buy - number))
                    ItemInfo.number = number


def reset_item():
    global ShopDiscount, Investment_lv1_precise, TomeOfKnowledge, Exp20_Range5, Exp40_Luck6, Locomotive
    global MasterChefHat, Helmet_32Luck_Precise, WitlessShako_Health_Precise, NorthWind_Luck13, Vtuber_Inves198_Speed7
    global Bicycle_lv3, Attack16_Arcane16, Attack16_Strike16, Critical30_Defense10, HealthRegen12_HitRecovery15
    global Holding_30HealthRegen, Luck60_Speed25, SplitTheVoid
    ShopDiscount.reset_item_number()
    Investment_lv1_precise.reset_item_number()
    TomeOfKnowledge.reset_item_number()
    Exp20_Range5.reset_item_number()
    Exp40_Luck6.reset_item_number()
    Locomotive.reset_item_number()
    MasterChefHat.reset_item_number()
    Helmet_32Luck_Precise.reset_item_number()
    WitlessShako_Health_Precise.reset_item_number()
    NorthWind_Luck13.reset_item_number()
    Vtuber_Inves198_Speed7.reset_item_number()
    Bicycle_lv3.reset_item_number()
    Attack16_Arcane16.reset_item_number()
    Attack16_Strike16.reset_item_number()
    Critical30_Defense10.reset_item_number()
    HealthRegen12_HitRecovery15.reset_item_number()
    Holding_30HealthRegen.reset_item_number()
    Luck60_Speed25.reset_item_number()
    SplitTheVoid.reset_item_number()


def buy_shop_discount():
    """
    This function is used to buy all items in the ShopDiscount category.
    """
    buy_item_info(ShopDiscount, 5)


def buy_investment_lv1_precise():
    """
    This function is used to buy all items in the Investment_lv1_precise category.
    """
    buy_item_info(Investment_lv1_precise, 5)


def buy_tome_of_knowledge():
    """
    This function is used to buy all items in the TomeOfKnowledge category.
    """
    buy_item_info(TomeOfKnowledge, 5)


def buy_exp20_range5():
    """
    This function is used to buy all items in the Exp20_Range5 category.
    """
    buy_item_info(Exp20_Range5, 5)


def buy_exp40_luck6():
    """
    This function is used to buy all items in the Exp40_Luck6 category.
    """
    buy_item_info(Exp40_Luck6, 5)


def buy_locomotive():
    """
    This function is used to buy all items in the Locomotive category.
    """
    buy_item_info(Locomotive, 5)


def buy_master_chef_hat():
    """
    This function is used to buy all items in the MasterChefHat category.
    """
    buy_item_info(MasterChefHat, 5)


def buy_bicycle_lv3():
    buy_item_info(Bicycle_lv3)


def buy_attack16_arcane16():
    buy_item_info(Attack16_Arcane16, 5)


def buy_attack16_strike16():
    buy_item_info(Attack16_Strike16, 5)


def buy_critical30_defense10():
    buy_item_info(Critical30_Defense10, 5)


def buy_health_regen12_hit_recovery15():
    buy_item_info(HealthRegen12_HitRecovery15, 5)


def buy_holding_30_health_regen():
    buy_item_info(Holding_30HealthRegen, 5)


def buy_luck60_speed25():
    buy_item_info(Luck60_Speed25, 5)


def buy_split_the_void():
    buy_item_info(SplitTheVoid, 5)


def buy_vtuber_inves198_speed7():
    buy_item_info(Vtuber_Inves198_Speed7, 5)


def buy_helmet_32_luck_precise():
    buy_item_info(Helmet_32Luck_Precise, 5)
