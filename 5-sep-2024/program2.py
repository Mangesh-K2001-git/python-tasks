class Earphone:
    def __init__(self,company,price,color,battery_life,char_type,touch_tap,sensor_touch):
        self.company = company
        self.price = price
        self.color=color
        self.battery_life=battery_life
        self.char_type=char_type
        self.touch_tap=touch_tap
        self.sensor_touch=sensor_touch
print("values for apple earphones")
apl1=Earphone("apple",25000,"white",2,"c_type","one","yes")
print("company:",apl1.company)
print("price:",apl1.price)
print("color:",apl1.color)
print("battery_life:",apl1.battery_life)
print("char_type:",apl1.char_type)
print("touch_tap:",apl1.touch_tap)
print("sensor_touch:",apl1.sensor_touch)

print("for new boat earphone")
apl2=Earphone("boat",13000,"black",3,"c_type","double","yes")
print("company:",apl2.company)
print("price:",apl2.price)
print("color:",apl2.color)
print("battery_life:",apl2.battery_life)
print("char_type:",apl2.char_type)
print("touch_tap:",apl2.touch_tap)
print("sensor_touch:",apl2.sensor_touch)



