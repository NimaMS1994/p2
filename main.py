from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy import Config
from kivy.uix.screenmanager import ScreenManager,Screen
import kivy
# import subprocess
Config.set('graphics', 'resizable', True)
# kivy.require('2.1.0') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.label import Label
import arabic_reshaper
from bidi.algorithm import get_display
from kivy.core.text import Label as CoreLabel
from kivy.core.image import Image
from kivy.uix.image import Image
from functools import partial
#from kivy.graphics import BorderImage
from kivy.graphics import Color, Rectangle
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
#from kivy.uix.image import AsyncImage
import tensorflow as tf
import numpy as np
from keras.models import load_model


# always_color = (0, 0, 2, 1)
# usually_color = (0, 2, 0, 1)
# sometimes_color = (100, 1, 0, 1)
# rarely_color = (1, 0, 0, 1)
# never_color = (1, 0, 1, 1)

always_color = (0, 0, 2, 1)
usually_color = (0, 2, 0, 1)
sometimes_color = (100, 1, 0, 1)
rarely_color = (1, 0, 0, 1)
never_color = (1, 0, 1, 1)
count = 0
start_statement = "ضمن عرض سلام خدمت ورزشکاران گرامی                 \nاین نرم افزار مربوط به سنجش قوای ذهنی ورزشکاران سیزم است.     \n خواهشمند است جهت حصول نتایج مطلوب، وقت‌گذاری و همکاری بفرمایید."
question1 = "1 ـ چیزی را پیدا می‌کنم که به من انگیزه دهد."
question2 = "2 ـ احساس می‌کنم نسبت به پیرامونم کنترل خوبی دارم."
question3 = "3 ـ چالش‌ها، بهترین‌ها را در من به وجود می آورند."
question4 = "4 ـ وقتی با دیگران کار می‌کنم، اثرگذار هستم."
question5 = "5 ـ تغییرات غیرمنتظره در برنامه، باعث ناراحتی من می‌شود."
question6 = "6 ـ تحت فشار تسلیم نمی‌شوم."
question7 = "7 ـ به توانایی‌های خودم اطمینان دارم."
question8 = "8 ـ احساس می‌کنم همه چیز آن‌طور که باید پیش نمی‌رود."
question9 = "9 ـ ((نمی‌دانم از کجا شروع کنم))احساسی است که وقتی چندین کار را همزمان انجام می‌دهم دارم."
question10 = "10 ـ آرزو می‌کنم که زندگی‌ام قابل پیش‌بینی‌تر بود."
question11 = "11 ـ به جنبه‌های روشن زندگی نگاه می‌کنم."
question12 = "12 ـ وقتی حرفی برای گفتن دارم، حرفم را می‌زنم."
question13 = "13 ـ می‌توان برای تکمیل وظایفی که به من داده می‌شود، به من اعتماد کرد."
question14 = "14 ـ با هر مشکلی که پیش می‌آید، به خوبی کنار می‌آیم."
question15 = "15 ـ از خودم انتقاد نمی‌کنم، حتی زمانی که همه چیز اشتباه شود."
question16 = "16 ـ در جمع‌های اجتماعی احساس ترس می‌کنم."
question17 = "17 ـ اگر مشکلی پیش بیاید، ادامه تلاشم کٌند می‌شود."
question18 = "18 ـ گویی اتفاق‌ها برای من می‌افتند."
question19 = "19 ـ عموماً احساساتم را از دیگران پنهان می‌کنم."
question20 = "20 ـ وقتی خسته هستم تلاش ذهنی برایم سخت است."
question21 = "21 ـ وقتی اشتباه می‌کنم، اجازه می‌دهم که تا روزها نگران بمانم."
question22 = "22 ـ می‌توانم سطوح بالایی از تلاش ذهنی را برای دوره‌های طولانی حفظ کنم."
question23 = "23 ـ از بحث کردن با کسی که اشتباه می‌کند، می‌ترسم."
question24 = "24 ـ می‌توانم عصبانیت خود را کنترل کنم."
question25 = "25 ـ وقتی با شکست مواجه می‌شوم، می‌توانم بر روی هدفم پافشاری کنم."
question26 = "26 ـ در ورزش کردن پشتکار دارم، حتی زمانی که بسیار احساس خستگی می‌کنم."
question27 = "27 ـ برای ورزش کردن اهداف تعیین می‌کنم."
question28 = "28 ـ اگر اعتماد به نفس خود را در حین مسابقه از دست دهم، می‌دانم چطور آن را بازسازی کنم."
question29 = "29 ـ زمان‌های مشخصی را جهت تمرین و ورزش در ذهنم تعیین و اجرا می‌کنم."
question30 = "30 ـ اگر شانس‌ها برای پیروزی کم باشد، قادرم بهترین تلاش خود را انجام دهم."
question31 = "31 ـ در رقابت‌های مهم نگرانم که مرتکب اشتباه شوم."
question32 = "32 ـ از رقابت‌های مهم می‌ترسم."
question33 = "33 ـ توانایی تصویرسازی ذهنی از کیفیت ورزشم را برای آینده دارم."
question34 = "34 ـ اگر در یک مسابقه عَقب بی‌افتم، احساس می‌کنم باز هم پیروزی ممکن است."
question35 = "35 ـ هر چقدر مسابقه اهمیت بیشتری داشته باشد، برای من لذت‌بخش‌تر است."
question36 = "36 ـ در حین رقابت‌های حساس مشکل تمرکز دارم."
question37 = "37 ـ قادرم به سرعت بعد از عملکرد ناامید کننده، خود را بازسازی کنم."
question38 = "38 ـ اهداف ورزشی خود را یادداشت می‌کنم."
question39 = "39 ـ بر روند پیشرفت اهدافم نظارت می‌کنم."
question40 = "40 ـ انگیزه دارم تا در تمرین و مسابقه برتری داشته باشم."
question41 = "41 ـ مقابله کردن با شکست‌ها و کنترل کردن شرایط دشوار را در ذهنم مرور می‌کنم."
question42 = "42 ـ زمانی که عملکرد ضعیفی دارم، اعتماد به نفسم به سرعت کاهش پیدا می‌کند."
question43 = "43 ـ در حین مسابقاتِ حساس، سخنان منفی دیگران(مانند تماشاگران یا حریفان) باعث ناراحتی‌ام می‌شود."
question44 = "44 ـ خود را یک مبارز سرسخت می‌دانم."
question45 = "45 ـ به طور واضح می‌توانم عملکردهای ورزشی قبلی خود را در ذهنم تجسم کنم."
question46 = "46 ـ دو ساعت بعد از غذا را بهترین زمان خواب می‌دانم."
question47 = "47 ـ نوع تغذیه می‌تواند بر کیفیت خوابتان اثرگذار باشد؟"
question48 = "48 ـ کمبود خواب می‌تواند در عملکرد روزانه و میزان انرژیتان اثرگذار باشد؟"
question49 = "49 ـ آیا شرایط محیطی(سروصدا، نور و جای مناسب) بر کیفیت خواب شما اثرگذار است؟"
question50 = "50 ـ مصرف میوه و سبزیجات بر چه مبنایی در رژیم غذایی روزانه‌تان قرار دارد؟"
question51 = "51 ـ مصرف مایعات بر چه مبنایی در برنامه روزانه شما قرار دارد؟"
question52 = "52 ـ آیا برای داشتن یک برنامه مطلوب و نتیجه‌بخش در استراحت، تمرین و تغذیه، از مشاور یا متخصص بهره‌مند می‌شوید؟"
question53 = "53 ـ استفاده از آزمایشات دوره‌ای را تا چه اندازه برای آگاهی از میزان سلامتی خود مطلوب می‌دانید؟"
question54 = "54 ـ فاکتور قد، سن و وزن را در تمرین، مسابقه و میزان موفقیت خود، چقدر موثر می‌دانید؟"
question55 = "55 ـ کدامیک از گزینه‌ها، در بازدهی، نشاط و شادابی شما پس از تمرین تاثیر بیشتری دارد؟"
question56 = "56 ـ فکر می‌کنید نسبت به اطلاعات مربوط به رشته تمرینی، نوع تغذیه و حفظ سلامتی خود به روز هستید؟"
question57 = "57 ـ دلیل انتخاب شما در رشته تمرینیتان بر چه اساس بوده است؟"
Questions = [question1,question2,question3,question4,question5,question6,question7,question8,question9,question10,question11,question12,question13,
             question14,question15,question16,question17,question18,question19,question20,question21,question22,question23,question24,question25,
             question26,question27,question28,question29,question30,question31,question32,question33,question34,question35,question36,question37,
             question38,question39,question40,question41,question42,question43,question44,question45,question46,question47,question48,question49,
             question50,question51,question52,question53,question54,question55,question56,question57]
class Relative_Layout_1(App):
    A = []

    #دکمه هرگز #######
    def never(self,instance):
        global count
        if count != 57:
            self.A.append(0)
            print("len A:", len(self.A))
            # global count
            count = count + 1
            print("count:", count)
            if count != 57:
                temp = arabic_reshaper.reshape(Questions[count])
                print("question number:", temp)
                temp_text = get_display(temp)
                print("temp_text:", temp_text)
                self.l1.text = temp_text

        if count == 49:
            temp = arabic_reshaper.reshape("بر اساس میزان کالری و انرژی")
            temp_text = get_display(temp)
            self.b1.text = temp_text
            temp = arabic_reshaper.reshape("بر حسب تعداد وعده")
            temp_text = get_display(temp)
            self.b2.text = temp_text
            temp = arabic_reshaper.reshape("به تناسب ذائقه و میل")
            temp_text = get_display(temp)
            self.b3.text = temp_text
            temp = arabic_reshaper.reshape("به تناسب هزینه")
            temp_text = get_display(temp)
            self.b4.text = temp_text
            temp = arabic_reshaper.reshape("تمام موارد")
            temp_text = get_display(temp)
            self.b5.text = temp_text
            self.b4.disabled = False
            self.b5.disabled = False


        if (count == 51 or count == 53 or count == 55):
            temp = arabic_reshaper.reshape("هرگز")
            temp_text = get_display(temp)
            self.b1.text = temp_text
            temp = arabic_reshaper.reshape("به ندرت")
            temp_text = get_display(temp)
            self.b2.text = temp_text
            temp = arabic_reshaper.reshape("گاهی")
            temp_text = get_display(temp)
            self.b3.text = temp_text
            temp = arabic_reshaper.reshape("اغلب")
            temp_text = get_display(temp)
            self.b4.text = temp_text
            self.b4.background_color = usually_color
            always_text = arabic_reshaper.reshape("همیشه")
            always_text_persian = get_display(always_text)
            self.b5.text = always_text_persian
            self.b5.background_color = always_color
            self.b5.disabled = False
            self.b4.disabled = False

        if count == 50:
            temp = arabic_reshaper.reshape("با توجه به فعالیت و کار روزانه")
            temp_text = get_display(temp)
            self.b1.text = temp_text
            temp = arabic_reshaper.reshape("هشت تا 12 لیوان در روز")
            temp_text = get_display(temp)
            self.b2.text = temp_text
            temp = arabic_reshaper.reshape("شدت و زمان ورزش")
            temp_text = get_display(temp)
            self.b3.text = temp_text
            temp = arabic_reshaper.reshape("تمام موارد")
            temp_text = get_display(temp)
            self.b4.text = temp_text
            self.b4.disabled = False
            self.b5.disabled = True
            self.b5.text = ""
            self.b5.background_color = (0, 0, 0, 0)

        if count == 52:
            temp = arabic_reshaper.reshape("هر ماه یکبار")
            temp_text = get_display(temp)
            self.b1.text = temp_text
            temp = arabic_reshaper.reshape("هر سه ماه یکبار")
            temp_text = get_display(temp)
            self.b2.text = temp_text
            temp = arabic_reshaper.reshape("هر شش ماه یکبار")
            temp_text = get_display(temp)
            self.b3.text = temp_text
            temp = arabic_reshaper.reshape("با مشورت پزشک متخصص")
            temp_text = get_display(temp)
            self.b4.text = temp_text
            self.b4.disabled = False
            self.b5.disabled = True
            self.b5.text = ""
            self.b5.background_color = (0, 0, 0, 0)

        if count == 54:
            temp = arabic_reshaper.reshape("تمرین فردی")
            temp_text = get_display(temp)
            self.b1.text = temp_text
            temp = arabic_reshaper.reshape("تمرین های دونفره")
            temp_text = get_display(temp)
            self.b2.text = temp_text
            temp = arabic_reshaper.reshape("تمرین های گروهی")
            temp_text = get_display(temp)
            self.b3.text = temp_text
            self.b4.disabled = True
            self.b4.text = ""
            self.b4.background_color = (0, 0, 0, 0)
            self.b5.disabled = True
            self.b5.text = ""
            self.b5.background_color = (0, 0, 0, 0)

        if count == 56:
            temp = arabic_reshaper.reshape("کشف ذوق، علاقه و استعداد فردی")
            temp_text = get_display(temp)
            self.b1.text = temp_text
            self.b1.font_size="20sp"
            temp = arabic_reshaper.reshape("امکانات و همه گیری در سطح شهر یا کشور")
            temp_text = get_display(temp)
            self.b2.text = temp_text
            self.b2.font_size="20sp"
            temp = arabic_reshaper.reshape("موفقیت و نام آوری بزرگان، خانواده یا فامیل")
            temp_text = get_display(temp)
            self.b3.text = temp_text
            self.b3.font_size="20sp"
            temp = arabic_reshaper.reshape("میزان هزینه")
            temp_text = get_display(temp)
            self.b4.text = temp_text
            self.b4.font_size="30sp"
            self.b4.background_color = usually_color
            self.b4.disabled = False
            self.b5.disabled = True
            self.b5.text = ""
            self.b5.background_color = (0, 0, 0, 0)

        if count == 57:
            self.b1.disabled = True
            self.b1.text = ""
            self.b1.background_color = (0, 0, 0, 0)
            self.b2.disabled = True
            self.b2.text = ""
            self.b2.background_color = (0, 0, 0, 0)
            self.b3.disabled = True
            self.b3.text = ""
            self.b3.background_color = (0, 0, 0, 0)
            self.b4.disabled = True
            self.b4.text = ""
            self.b4.background_color = (0, 0, 0, 0)
            self.b5.disabled = True
            self.b5.text = ""
            self.b5.background_color = (0, 0, 0, 0)

            ################### sleep class
            immatrix = []
            immatrix.append(self.A)
            immatrix = np.asarray(immatrix)
            immatrix = immatrix.astype('float32', copy=False)
            immatrix /= 4
            model_sleep = load_model('class sleep model.h5')
            model_sleep.summary()
            predict_sleep = model_sleep.predict(immatrix , verbose=1)
            final_predict_sleep = np.argmax(predict_sleep, axis=1)
            if final_predict_sleep == 0:
                temp = arabic_reshaper.reshape("2 ـ ورزشکار گرامی باید میزان خواب کافی را در شبانه روز در اولویت قرار دهید.")
                temp_text = get_display(temp)
                self.l1.text = temp_text
            if final_predict_sleep == 1:
                temp = arabic_reshaper.reshape("2 ـ ورزشکار گرامی سطح خواب شما در شبانه روز در حد متوسط است و باید مقداری ساعات خواب خود را افزایش دهید.")
                temp_text = get_display(temp)
                self.l1.text = temp_text
            if final_predict_sleep == 2:
                temp = arabic_reshaper.reshape( "2 ـ ورزشکار گرامی سطح خواب شما عالی است.")
                temp_text = get_display(temp)
                self.l1.text = temp_text

            ################### geography class
            immatrix = []
            immatrix.append(self.A)
            immatrix = np.asarray(immatrix)
            immatrix = immatrix.astype('float32', copy=False)
            immatrix /= 4
            model = load_model('geography class model.h5')
            model.summary()
            predict = model.predict(immatrix, verbose=1)
            final_predict = np.argmax(predict, axis=1)
            if final_predict == 0:
                temp = arabic_reshaper.reshape(
                        "1 ـ ورزشکار گرامی موقعیت جغرافیایی (آب و هوا، طبیعت و ...) به شدت در روحیه و بازدهی تمرین شما اثر گذار است.")
                temp_text = get_display(temp)
                self.l2.text = temp_text
            if final_predict == 1:
                temp = arabic_reshaper.reshape(
                        "1 ـ ورزشکار گرامی موقعیت جغرافیایی (آب و هوا، طبیعت و ...) تاثیر نسبی در روحیه و بازدهی تمرین شما اثر گذار است.")
                temp_text = get_display(temp)
                self.l2.text = temp_text
            if final_predict == 2:
                temp = arabic_reshaper.reshape(
                        "1 ـ ورزشکار گرامی موقعیت جغرافیایی (آب و هوا، طبیعت و ...) تاثیری در روحیه و بازدهی تمرین شما ندارد.")
                temp_text = get_display(temp)
                self.l2.text = temp_text

            ################### parallel class
            immatrix = []
            immatrix.append(self.A)
            immatrix = np.asarray(immatrix)
            immatrix = immatrix.astype('float32', copy=False)
            immatrix /= 4
            model = load_model('parallel class model.h5')
            model.summary()
            predict = model.predict(immatrix, verbose=1)
            final_predict = np.argmax(predict, axis=1)
            if final_predict == 0:
                temp = arabic_reshaper.reshape(
                        "3 ـ ورزشکار گرامی شما از رشته های موازی ورزشی استفاده ای نمی کنید.")
                temp_text = get_display(temp)
                self.l3.text = temp_text
            if final_predict == 1:
                temp = arabic_reshaper.reshape(
                        "3 ـ ورزشکار گرامی شما به طور نسبی از رشته های موازی ورزشی استفاده می کنید.")
                temp_text = get_display(temp)
                self.l3.text = temp_text
            if final_predict == 2:
                temp = arabic_reshaper.reshape(
                        "3 ـ ورزشکار گرامی شما از رشته های موازی ورزشی به خوبی بهره می برید.")
                temp_text = get_display(temp)
                self.l3.text = temp_text

            ################### technology class
            immatrix = []
            immatrix.append(self.A)
            immatrix = np.asarray(immatrix)
            immatrix = immatrix.astype('float32', copy=False)
            immatrix /= 4
            model = load_model('technology class model.h5')
            model.summary()
            predict = model.predict(immatrix, verbose=1)
            final_predict = np.argmax(predict, axis=1)
            if final_predict == 0:
                temp = arabic_reshaper.reshape(
                        "4 ـ ورزشکار گرامی شما از تکنولوژی جدید ورزشی بهره ای نمی برید. ")
                temp_text = get_display(temp)
                self.l4.text = temp_text
            if final_predict == 1:
                temp = arabic_reshaper.reshape(
                        "4 ـ ورزشکار گرامی شما از تکنولوژی جدید ورزشی به طور نسبی استفاده می کنید. ")
                temp_text = get_display(temp)
                self.l4.text = temp_text
            if final_predict == 2:
                temp = arabic_reshaper.reshape(
                        "4 ـ ورزشکار گرامی شما از تکنولوژی جدید ورزشی بهره به خوبی بهره می برید. ")
                temp_text = get_display(temp)
                self.l4.text = temp_text

            ################### time of exercise
            immatrix = []
            immatrix.append(self.A)
            immatrix = np.asarray(immatrix)
            immatrix = immatrix.astype('float32', copy=False)
            immatrix /= 4
            model = load_model('time of exercise model.h5')
            model.summary()
            predict = model.predict(immatrix, verbose=1)
            final_predict = np.argmax(predict, axis=1)
            if final_predict == 0:
                temp = arabic_reshaper.reshape(
                        "5 ـ ورزشکار گرامی شما تمایل دارید که صبح ها ورزش کنید.")
                temp_text = get_display(temp)
                self.l5.text = temp_text
            if final_predict == 1:
                temp = arabic_reshaper.reshape(
                        "5 ـ ورزشکار گرامی شما تمایل دارید که در بعد از ظهر ورزش کنید و لازم است که صبح ورزش کنید.")
                temp_text = get_display(temp)
                self.l5.text = temp_text
            if final_predict == 2:
                temp = arabic_reshaper.reshape(
                        "5 ـ ورزشکار گرامی برای شما اهمیتی ندارد که صبح ها یا بعد از ظهر ها ورزش کنید. ولی توصیه می شود که صبح ها ورزش کنید. ")
                temp_text = get_display(temp)
                self.l5.text = temp_text

    #دکمه به ندرت #######
    def rarely(self,instance):
        global count
        if count != 57:
            self.A.append(1)
            print("len A:", len(self.A))
            # global count
            count = count + 1
            print("count:", count)
            if count != 57:
                temp = arabic_reshaper.reshape(Questions[count])
                print("question number:", temp)
                temp_text = get_display(temp)
                print("temp_text:", temp_text)
                self.l1.text = temp_text

        if count == 49:
            temp = arabic_reshaper.reshape("بر اساس میزان کالری و انرژی")
            temp_text = get_display(temp)
            self.b1.text = temp_text
            temp = arabic_reshaper.reshape("بر حسب تعداد وعده")
            temp_text = get_display(temp)
            self.b2.text = temp_text
            temp = arabic_reshaper.reshape("به تناسب ذائقه و میل")
            temp_text = get_display(temp)
            self.b3.text = temp_text
            temp = arabic_reshaper.reshape("به تناسب هزینه")
            temp_text = get_display(temp)
            self.b4.text = temp_text
            temp = arabic_reshaper.reshape("تمام موارد")
            temp_text = get_display(temp)
            self.b5.text = temp_text
            self.b4.disabled = False
            self.b5.disabled = False

        if (count == 51 or count == 53 or count == 55):
            temp = arabic_reshaper.reshape("هرگز")
            temp_text = get_display(temp)
            self.b1.text = temp_text
            temp = arabic_reshaper.reshape("به ندرت")
            temp_text = get_display(temp)
            self.b2.text = temp_text
            temp = arabic_reshaper.reshape("گاهی")
            temp_text = get_display(temp)
            self.b3.text = temp_text
            temp = arabic_reshaper.reshape("اغلب")
            temp_text = get_display(temp)
            self.b4.text = temp_text
            self.b4.background_color = usually_color
            always_text = arabic_reshaper.reshape("همیشه")
            always_text_persian = get_display(always_text)
            self.b5.text = always_text_persian
            self.b5.background_color = always_color
            self.b5.disabled = False
            self.b4.disabled = False

        if count == 50:
            temp = arabic_reshaper.reshape("با توجه به فعالیت و کار روزانه")
            temp_text = get_display(temp)
            self.b1.text = temp_text
            temp = arabic_reshaper.reshape("هشت تا 12 لیوان در روز")
            temp_text = get_display(temp)
            self.b2.text = temp_text
            temp = arabic_reshaper.reshape("شدت و زمان ورزش")
            temp_text = get_display(temp)
            self.b3.text = temp_text
            temp = arabic_reshaper.reshape("تمام موارد")
            temp_text = get_display(temp)
            self.b4.text = temp_text
            self.b4.disabled = False
            self.b5.disabled = True
            self.b5.text = ""
            self.b5.background_color = (0, 0, 0, 0)

        if count == 52:
            temp = arabic_reshaper.reshape("هر ماه یکبار")
            temp_text = get_display(temp)
            self.b1.text = temp_text
            temp = arabic_reshaper.reshape("هر سه ماه یکبار")
            temp_text = get_display(temp)
            self.b2.text = temp_text
            temp = arabic_reshaper.reshape("هر شش ماه یکبار")
            temp_text = get_display(temp)
            self.b3.text = temp_text
            temp = arabic_reshaper.reshape("با مشورت پزشک متخصص")
            temp_text = get_display(temp)
            self.b4.text = temp_text
            self.b4.disabled = False
            self.b5.disabled = True
            self.b5.text = ""
            self.b5.background_color = (0, 0, 0, 0)

        if count == 54:
            temp = arabic_reshaper.reshape("تمرین فردی")
            temp_text = get_display(temp)
            self.b1.text = temp_text
            temp = arabic_reshaper.reshape("تمرین های دونفره")
            temp_text = get_display(temp)
            self.b2.text = temp_text
            temp = arabic_reshaper.reshape("تمرین های گروهی")
            temp_text = get_display(temp)
            self.b3.text = temp_text
            self.b4.disabled = True
            self.b4.text = ""
            self.b4.background_color = (0, 0, 0, 0)
            self.b5.disabled = True
            self.b5.text = ""
            self.b5.background_color = (0, 0, 0, 0)

        if count == 56:
            temp = arabic_reshaper.reshape("کشف ذوق، علاقه و استعداد فردی")
            temp_text = get_display(temp)
            self.b1.text = temp_text
            self.b1.font_size="25sp"
            temp = arabic_reshaper.reshape("امکانات و همه گیری در سطح شهر یا کشور")
            temp_text = get_display(temp)
            self.b2.text = temp_text
            self.b2.font_size="25sp"
            temp = arabic_reshaper.reshape("موفقیت و نام آوری بزرگان، خانواده یا فامیل")
            temp_text = get_display(temp)
            self.b3.text = temp_text
            self.b3.font_size="25sp"
            temp = arabic_reshaper.reshape("میزان هزینه")
            temp_text = get_display(temp)
            self.b4.text = temp_text
            self.b4.font_size="30sp"
            self.b4.background_color = usually_color
            self.b4.disabled = False
            self.b5.disabled = True
            self.b5.text = ""
            self.b5.background_color = (0, 0, 0, 0)

        if count == 57:
            self.b1.disabled = True
            self.b1.text = ""
            self.b1.background_color = (0, 0, 0, 0)
            self.b2.disabled = True
            self.b2.text = ""
            self.b2.background_color = (0, 0, 0, 0)
            self.b3.disabled = True
            self.b3.text = ""
            self.b3.background_color = (0, 0, 0, 0)
            self.b4.disabled = True
            self.b4.text = ""
            self.b4.background_color = (0, 0, 0, 0)
            self.b5.disabled = True
            self.b5.text = ""
            self.b5.background_color = (0, 0, 0, 0)

            ################### sleep class
            immatrix = []
            immatrix.append(self.A)
            immatrix = np.asarray(immatrix)
            immatrix = immatrix.astype('float32', copy=False)
            immatrix /= 4
            model_sleep = load_model('class sleep model.h5')
            model_sleep.summary()
            predict_sleep = model_sleep.predict(immatrix, verbose=1)
            final_predict_sleep = np.argmax(predict_sleep, axis=1)
            if final_predict_sleep == 0:
                temp = arabic_reshaper.reshape(
                    "2 ـ ورزشکار گرامی باید میزان خواب کافی را در شبانه روز در اولویت قرار دهید.")
                temp_text = get_display(temp)
                self.l1.text = temp_text
            if final_predict_sleep == 1:
                temp = arabic_reshaper.reshape(
                    "2 ـ ورزشکار گرامی سطح خواب شما در شبانه روز در حد متوسط است و باید مقداری ساعات خواب خود را افزایش دهید.")
                temp_text = get_display(temp)
                self.l1.text = temp_text
            if final_predict_sleep == 2:
                temp = arabic_reshaper.reshape("2 ـ ورزشکار گرامی سطح خواب شما عالی است.")
                temp_text = get_display(temp)
                self.l1.text = temp_text

            ################### geography class
            immatrix = []
            immatrix.append(self.A)
            immatrix = np.asarray(immatrix)
            immatrix = immatrix.astype('float32', copy=False)
            immatrix /= 4
            model = load_model('geography class model.h5')
            model.summary()
            predict = model.predict(immatrix, verbose=1)
            final_predict = np.argmax(predict, axis=1)
            if final_predict == 0:
                temp = arabic_reshaper.reshape(
                    "1 ـ ورزشکار گرامی موقعیت جغرافیایی (آب و هوا، طبیعت و ...) به شدت در روحیه و بازدهی تمرین شما اثر گذار است.")
                temp_text = get_display(temp)
                self.l2.text = temp_text
            if final_predict == 1:
                temp = arabic_reshaper.reshape(
                    "1 ـ ورزشکار گرامی موقعیت جغرافیایی (آب و هوا، طبیعت و ...) تاثیر نسبی در روحیه و بازدهی تمرین شما اثر گذار است.")
                temp_text = get_display(temp)
                self.l2.text = temp_text
            if final_predict == 2:
                temp = arabic_reshaper.reshape(
                    "1 ـ ورزشکار گرامی موقعیت جغرافیایی (آب و هوا، طبیعت و ...) تاثیری در روحیه و بازدهی تمرین شما ندارد.")
                temp_text = get_display(temp)
                self.l2.text = temp_text

            ################### parallel class
            immatrix = []
            immatrix.append(self.A)
            immatrix = np.asarray(immatrix)
            immatrix = immatrix.astype('float32', copy=False)
            immatrix /= 4
            model = load_model('parallel class model.h5')
            model.summary()
            predict = model.predict(immatrix, verbose=1)
            final_predict = np.argmax(predict, axis=1)
            if final_predict == 0:
                temp = arabic_reshaper.reshape(
                    "3 ـ ورزشکار گرامی شما از رشته های موازی ورزشی استفاده ای نمی کنید.")
                temp_text = get_display(temp)
                self.l3.text = temp_text
            if final_predict == 1:
                temp = arabic_reshaper.reshape(
                    "3 ـ ورزشکار گرامی شما به طور نسبی از رشته های موازی ورزشی استفاده می کنید.")
                temp_text = get_display(temp)
                self.l3.text = temp_text
            if final_predict == 2:
                temp = arabic_reshaper.reshape(
                    "3 ـ ورزشکار گرامی شما از رشته های موازی ورزشی به خوبی بهره می برید.")
                temp_text = get_display(temp)
                self.l3.text = temp_text

            ################### technology class
            immatrix = []
            immatrix.append(self.A)
            immatrix = np.asarray(immatrix)
            immatrix = immatrix.astype('float32', copy=False)
            immatrix /= 4
            model = load_model('technology class model.h5')
            model.summary()
            predict = model.predict(immatrix, verbose=1)
            final_predict = np.argmax(predict, axis=1)
            if final_predict == 0:
                temp = arabic_reshaper.reshape(
                    "4 ـ ورزشکار گرامی شما از تکنولوژی جدید ورزشی بهره ای نمی برید. ")
                temp_text = get_display(temp)
                self.l4.text = temp_text
            if final_predict == 1:
                temp = arabic_reshaper.reshape(
                    "4 ـ ورزشکار گرامی شما از تکنولوژی جدید ورزشی به طور نسبی استفاده می کنید. ")
                temp_text = get_display(temp)
                self.l4.text = temp_text
            if final_predict == 2:
                temp = arabic_reshaper.reshape(
                    "4 ـ ورزشکار گرامی شما از تکنولوژی جدید ورزشی بهره به خوبی بهره می برید. ")
                temp_text = get_display(temp)
                self.l4.text = temp_text

            ################### time of exercise
            immatrix = []
            immatrix.append(self.A)
            immatrix = np.asarray(immatrix)
            immatrix = immatrix.astype('float32', copy=False)
            immatrix /= 4
            model = load_model('time of exercise model.h5')
            model.summary()
            predict = model.predict(immatrix, verbose=1)
            final_predict = np.argmax(predict, axis=1)
            if final_predict == 0:
                temp = arabic_reshaper.reshape(
                    "5 ـ ورزشکار گرامی شما تمایل دارید که صبح ها ورزش کنید.")
                temp_text = get_display(temp)
                self.l5.text = temp_text
            if final_predict == 1:
                temp = arabic_reshaper.reshape(
                    "5 ـ ورزشکار گرامی شما تمایل دارید که در بعد از ظهر ورزش کنید و لازم است که صبح ورزش کنید.")
                temp_text = get_display(temp)
                self.l5.text = temp_text
            if final_predict == 2:
                temp = arabic_reshaper.reshape(
                    "5 ـ ورزشکار گرامی برای شما اهمیتی ندارد که صبح ها یا بعد از ظهر ها ورزش کنید. ولی توصیه می شود که صبح ها ورزش کنید. ")
                temp_text = get_display(temp)
                self.l5.text = temp_text

    #دکمه گاهی #######
    def sometimes(self,instance):
        global count
        if count != 57:
            self.A.append(2)
            print("len A:", len(self.A))
            # global count
            count = count + 1
            print("count:", count)
            if count != 57:
                temp = arabic_reshaper.reshape(Questions[count])
                print("question number:", temp)
                temp_text = get_display(temp)
                print("temp_text:", temp_text)
                self.l1.text = temp_text

        if count == 49:
            temp = arabic_reshaper.reshape("بر اساس میزان کالری و انرژی")
            temp_text = get_display(temp)
            self.b1.text = temp_text
            temp = arabic_reshaper.reshape("بر حسب تعداد وعده")
            temp_text = get_display(temp)
            self.b2.text = temp_text
            temp = arabic_reshaper.reshape("به تناسب ذائقه و میل")
            temp_text = get_display(temp)
            self.b3.text = temp_text
            temp = arabic_reshaper.reshape("به تناسب هزینه")
            temp_text = get_display(temp)
            self.b4.text = temp_text
            temp = arabic_reshaper.reshape("تمام موارد")
            temp_text = get_display(temp)
            self.b5.text = temp_text
            self.b4.disabled = False
            self.b5.disabled = False

        if (count == 51 or count == 53 or count == 55):
            temp = arabic_reshaper.reshape("هرگز")
            temp_text = get_display(temp)
            self.b1.text = temp_text
            temp = arabic_reshaper.reshape("به ندرت")
            temp_text = get_display(temp)
            self.b2.text = temp_text
            temp = arabic_reshaper.reshape("گاهی")
            temp_text = get_display(temp)
            self.b3.text = temp_text
            temp = arabic_reshaper.reshape("اغلب")
            temp_text = get_display(temp)
            self.b4.text = temp_text
            self.b4.background_color = usually_color
            always_text = arabic_reshaper.reshape("همیشه")
            always_text_persian = get_display(always_text)
            self.b5.text = always_text_persian
            self.b5.background_color = always_color
            self.b5.disabled = False
            self.b4.disabled = False

        if count == 50:
            temp = arabic_reshaper.reshape("با توجه به فعالیت و کار روزانه")
            temp_text = get_display(temp)
            self.b1.text = temp_text
            temp = arabic_reshaper.reshape("هشت تا 12 لیوان در روز")
            temp_text = get_display(temp)
            self.b2.text = temp_text
            temp = arabic_reshaper.reshape("شدت و زمان ورزش")
            temp_text = get_display(temp)
            self.b3.text = temp_text
            temp = arabic_reshaper.reshape("تمام موارد")
            temp_text = get_display(temp)
            self.b4.text = temp_text
            self.b4.disabled = False
            self.b5.disabled = True
            self.b5.text = ""
            self.b5.background_color = (0, 0, 0, 0)

        if count == 52:
            temp = arabic_reshaper.reshape("هر ماه یکبار")
            temp_text = get_display(temp)
            self.b1.text = temp_text
            temp = arabic_reshaper.reshape("هر سه ماه یکبار")
            temp_text = get_display(temp)
            self.b2.text = temp_text
            temp = arabic_reshaper.reshape("هر شش ماه یکبار")
            temp_text = get_display(temp)
            self.b3.text = temp_text
            temp = arabic_reshaper.reshape("با مشورت پزشک متخصص")
            temp_text = get_display(temp)
            self.b4.text = temp_text
            self.b4.disabled = False
            self.b5.disabled = True
            self.b5.text = ""
            self.b5.background_color = (0, 0, 0, 0)

        if count == 54:
            temp = arabic_reshaper.reshape("تمرین فردی")
            temp_text = get_display(temp)
            self.b1.text = temp_text
            temp = arabic_reshaper.reshape("تمرین های دونفره")
            temp_text = get_display(temp)
            self.b2.text = temp_text
            temp = arabic_reshaper.reshape("تمرین های گروهی")
            temp_text = get_display(temp)
            self.b3.text = temp_text
            self.b4.disabled = True
            self.b4.text = ""
            self.b4.background_color = (0, 0, 0, 0)
            self.b5.disabled = True
            self.b5.text = ""
            self.b5.background_color = (0, 0, 0, 0)

        if count == 56:
            temp = arabic_reshaper.reshape("کشف ذوق، علاقه و استعداد فردی")
            temp_text = get_display(temp)
            self.b1.text = temp_text
            self.b1.font_size="25sp"
            temp = arabic_reshaper.reshape("امکانات و همه گیری در سطح شهر یا کشور")
            temp_text = get_display(temp)
            self.b2.text = temp_text
            self.b2.font_size="25sp"
            temp = arabic_reshaper.reshape("موفقیت و نام آوری بزرگان، خانواده یا فامیل")
            temp_text = get_display(temp)
            self.b3.text = temp_text
            self.b3.font_size="25sp"
            temp = arabic_reshaper.reshape("میزان هزینه")
            temp_text = get_display(temp)
            self.b4.text = temp_text
            self.b4.font_size="30sp"
            self.b4.background_color = usually_color
            self.b4.disabled = False
            self.b5.disabled = True
            self.b5.text = ""
            self.b5.background_color = (0, 0, 0, 0)

        if count == 57:
            self.b1.disabled = True
            self.b1.text = ""
            self.b1.background_color = (0, 0, 0, 0)
            self.b2.disabled = True
            self.b2.text = ""
            self.b2.background_color = (0, 0, 0, 0)
            self.b3.disabled = True
            self.b3.text = ""
            self.b3.background_color = (0, 0, 0, 0)
            self.b4.disabled = True
            self.b4.text = ""
            self.b4.background_color = (0, 0, 0, 0)
            self.b5.disabled = True
            self.b5.text = ""
            self.b5.background_color = (0, 0, 0, 0)

            ################### sleep class
            immatrix = []
            immatrix.append(self.A)
            immatrix = np.asarray(immatrix)
            immatrix = immatrix.astype('float32', copy=False)
            immatrix /= 4
            model_sleep = load_model('class sleep model.h5')
            model_sleep.summary()
            predict_sleep = model_sleep.predict(immatrix, verbose=1)
            final_predict_sleep = np.argmax(predict_sleep, axis=1)
            if final_predict_sleep == 0:
                temp = arabic_reshaper.reshape(
                    "2 ـ ورزشکار گرامی باید میزان خواب کافی را در شبانه روز در اولویت قرار دهید.")
                temp_text = get_display(temp)
                self.l1.text = temp_text
            if final_predict_sleep == 1:
                temp = arabic_reshaper.reshape(
                    "2 ـ ورزشکار گرامی سطح خواب شما در شبانه روز در حد متوسط است و باید مقداری ساعات خواب خود را افزایش دهید.")
                temp_text = get_display(temp)
                self.l1.text = temp_text
            if final_predict_sleep == 2:
                temp = arabic_reshaper.reshape("2 ـ ورزشکار گرامی سطح خواب شما عالی است.")
                temp_text = get_display(temp)
                self.l1.text = temp_text

            ################### geography class
            immatrix = []
            immatrix.append(self.A)
            immatrix = np.asarray(immatrix)
            immatrix = immatrix.astype('float32', copy=False)
            immatrix /= 4
            model = load_model('geography class model.h5')
            model.summary()
            predict = model.predict(immatrix, verbose=1)
            final_predict = np.argmax(predict, axis=1)
            if final_predict == 0:
                temp = arabic_reshaper.reshape(
                    "1 ـ ورزشکار گرامی موقعیت جغرافیایی (آب و هوا، طبیعت و ...) به شدت در روحیه و بازدهی تمرین شما اثر گذار است.")
                temp_text = get_display(temp)
                self.l2.text = temp_text
            if final_predict == 1:
                temp = arabic_reshaper.reshape(
                    "1 ـ ورزشکار گرامی موقعیت جغرافیایی (آب و هوا، طبیعت و ...) تاثیر نسبی در روحیه و بازدهی تمرین شما اثر گذار است.")
                temp_text = get_display(temp)
                self.l2.text = temp_text
            if final_predict == 2:
                temp = arabic_reshaper.reshape(
                    "1 ـ ورزشکار گرامی موقعیت جغرافیایی (آب و هوا، طبیعت و ...) تاثیری در روحیه و بازدهی تمرین شما ندارد.")
                temp_text = get_display(temp)
                self.l2.text = temp_text

            ################### parallel class
            immatrix = []
            immatrix.append(self.A)
            immatrix = np.asarray(immatrix)
            immatrix = immatrix.astype('float32', copy=False)
            immatrix /= 4
            model = load_model('parallel class model.h5')
            model.summary()
            predict = model.predict(immatrix, verbose=1)
            final_predict = np.argmax(predict, axis=1)
            if final_predict == 0:
                temp = arabic_reshaper.reshape(
                    "3 ـ ورزشکار گرامی شما از رشته های موازی ورزشی استفاده ای نمی کنید.")
                temp_text = get_display(temp)
                self.l3.text = temp_text
            if final_predict == 1:
                temp = arabic_reshaper.reshape(
                    "3 ـ ورزشکار گرامی شما به طور نسبی از رشته های موازی ورزشی استفاده می کنید.")
                temp_text = get_display(temp)
                self.l3.text = temp_text
            if final_predict == 2:
                temp = arabic_reshaper.reshape(
                    "3 ـ ورزشکار گرامی شما از رشته های موازی ورزشی به خوبی بهره می برید.")
                temp_text = get_display(temp)
                self.l3.text = temp_text

            ################### technology class
            immatrix = []
            immatrix.append(self.A)
            immatrix = np.asarray(immatrix)
            immatrix = immatrix.astype('float32', copy=False)
            immatrix /= 4
            model = load_model('technology class model.h5')
            model.summary()
            predict = model.predict(immatrix, verbose=1)
            final_predict = np.argmax(predict, axis=1)
            if final_predict == 0:
                temp = arabic_reshaper.reshape(
                    "4 ـ ورزشکار گرامی شما از تکنولوژی جدید ورزشی بهره ای نمی برید. ")
                temp_text = get_display(temp)
                self.l4.text = temp_text
            if final_predict == 1:
                temp = arabic_reshaper.reshape(
                    "4 ـ ورزشکار گرامی شما از تکنولوژی جدید ورزشی به طور نسبی استفاده می کنید. ")
                temp_text = get_display(temp)
                self.l4.text = temp_text
            if final_predict == 2:
                temp = arabic_reshaper.reshape(
                    "4 ـ ورزشکار گرامی شما از تکنولوژی جدید ورزشی بهره به خوبی بهره می برید. ")
                temp_text = get_display(temp)
                self.l4.text = temp_text

            ################### time of exercise
            immatrix = []
            immatrix.append(self.A)
            immatrix = np.asarray(immatrix)
            immatrix = immatrix.astype('float32', copy=False)
            immatrix /= 4
            model = load_model('time of exercise model.h5')
            model.summary()
            predict = model.predict(immatrix, verbose=1)
            final_predict = np.argmax(predict, axis=1)
            if final_predict == 0:
                temp = arabic_reshaper.reshape(
                    "5 ـ ورزشکار گرامی شما تمایل دارید که صبح ها ورزش کنید.")
                temp_text = get_display(temp)
                self.l5.text = temp_text
            if final_predict == 1:
                temp = arabic_reshaper.reshape(
                    "5 ـ ورزشکار گرامی شما تمایل دارید که در بعد از ظهر ورزش کنید و لازم است که صبح ورزش کنید.")
                temp_text = get_display(temp)
                self.l5.text = temp_text
            if final_predict == 2:
                temp = arabic_reshaper.reshape(
                    "5 ـ ورزشکار گرامی برای شما اهمیتی ندارد که صبح ها یا بعد از ظهر ها ورزش کنید. ولی توصیه می شود که صبح ها ورزش کنید. ")
                temp_text = get_display(temp)
                self.l5.text = temp_text

    #دکمه اغلب #######
    def usually(self,instance):
        global count
        if count != 57:
            self.A.append(3)
            print("len A:", len(self.A))
            # global count
            count = count + 1
            print("count:", count)
            if count != 57:
                temp = arabic_reshaper.reshape(Questions[count])
                print("question number:", temp)
                temp_text = get_display(temp)
                print("temp_text:", temp_text)
                self.l1.text = temp_text

        if count == 49:
            temp = arabic_reshaper.reshape("بر اساس میزان کالری و انرژی")
            temp_text = get_display(temp)
            self.b1.text = temp_text
            temp = arabic_reshaper.reshape("بر حسب تعداد وعده")
            temp_text = get_display(temp)
            self.b2.text = temp_text
            temp = arabic_reshaper.reshape("به تناسب ذائقه و میل")
            temp_text = get_display(temp)
            self.b3.text = temp_text
            temp = arabic_reshaper.reshape("به تناسب هزینه")
            temp_text = get_display(temp)
            self.b4.text = temp_text
            temp = arabic_reshaper.reshape("تمام موارد")
            temp_text = get_display(temp)
            self.b5.text = temp_text
            self.b4.disabled = False
            self.b5.disabled = False

        if (count == 51 or count == 53 or count == 55):
            temp = arabic_reshaper.reshape("هرگز")
            temp_text = get_display(temp)
            self.b1.text = temp_text
            temp = arabic_reshaper.reshape("به ندرت")
            temp_text = get_display(temp)
            self.b2.text = temp_text
            temp = arabic_reshaper.reshape("گاهی")
            temp_text = get_display(temp)
            self.b3.text = temp_text
            temp = arabic_reshaper.reshape("اغلب")
            temp_text = get_display(temp)
            self.b4.text = temp_text
            self.b4.background_color = usually_color
            always_text = arabic_reshaper.reshape("همیشه")
            always_text_persian = get_display(always_text)
            self.b5.text = always_text_persian
            self.b5.background_color = always_color
            self.b5.disabled = False
            self.b4.disabled = False

        if count == 50:
            temp = arabic_reshaper.reshape("با توجه به فعالیت و کار روزانه")
            temp_text = get_display(temp)
            self.b1.text = temp_text
            temp = arabic_reshaper.reshape("هشت تا 12 لیوان در روز")
            temp_text = get_display(temp)
            self.b2.text = temp_text
            temp = arabic_reshaper.reshape("شدت و زمان ورزش")
            temp_text = get_display(temp)
            self.b3.text = temp_text
            temp = arabic_reshaper.reshape("تمام موارد")
            temp_text = get_display(temp)
            self.b4.text = temp_text
            self.b4.disabled = False
            self.b5.disabled = True
            self.b5.text = ""
            self.b5.background_color = (0, 0, 0, 0)

        if count == 52:
            temp = arabic_reshaper.reshape("هر ماه یکبار")
            temp_text = get_display(temp)
            self.b1.text = temp_text
            temp = arabic_reshaper.reshape("هر سه ماه یکبار")
            temp_text = get_display(temp)
            self.b2.text = temp_text
            temp = arabic_reshaper.reshape("هر شش ماه یکبار")
            temp_text = get_display(temp)
            self.b3.text = temp_text
            temp = arabic_reshaper.reshape("با مشورت پزشک متخصص")
            temp_text = get_display(temp)
            self.b4.text = temp_text
            self.b4.disabled = False
            self.b5.disabled = True
            self.b5.text = ""
            self.b5.background_color = (0, 0, 0, 0)

        if count == 54:
            temp = arabic_reshaper.reshape("تمرین فردی")
            temp_text = get_display(temp)
            self.b1.text = temp_text
            temp = arabic_reshaper.reshape("تمرین های دونفره")
            temp_text = get_display(temp)
            self.b2.text = temp_text
            temp = arabic_reshaper.reshape("تمرین های گروهی")
            temp_text = get_display(temp)
            self.b3.text = temp_text
            self.b4.disabled = True
            self.b4.text = ""
            self.b4.background_color = (0, 0, 0, 0)
            self.b5.disabled = True
            self.b5.text = ""
            self.b5.background_color = (0, 0, 0, 0)

        if count == 56:
            temp = arabic_reshaper.reshape("کشف ذوق، علاقه و استعداد فردی")
            temp_text = get_display(temp)
            self.b1.text = temp_text
            self.b1.font_size="25sp"
            temp = arabic_reshaper.reshape("امکانات و همه گیری در سطح شهر یا کشور")
            temp_text = get_display(temp)
            self.b2.text = temp_text
            self.b2.font_size="25sp"
            temp = arabic_reshaper.reshape("موفقیت و نام آوری بزرگان، خانواده یا فامیل")
            temp_text = get_display(temp)
            self.b3.text = temp_text
            self.b3.font_size="25sp"
            temp = arabic_reshaper.reshape("میزان هزینه")
            temp_text = get_display(temp)
            self.b4.text = temp_text
            self.b4.font_size="30sp"
            self.b4.background_color = usually_color
            self.b4.disabled = False
            self.b5.disabled = True
            self.b5.text = ""
            self.b5.background_color = (0, 0, 0, 0)

        if count == 57:
            self.b1.disabled = True
            self.b1.text = ""
            self.b1.background_color = (0, 0, 0, 0)
            self.b2.disabled = True
            self.b2.text = ""
            self.b2.background_color = (0, 0, 0, 0)
            self.b3.disabled = True
            self.b3.text = ""
            self.b3.background_color = (0, 0, 0, 0)
            self.b4.disabled = True
            self.b4.text = ""
            self.b4.background_color = (0, 0, 0, 0)
            self.b5.disabled = True
            self.b5.text = ""
            self.b5.background_color = (0, 0, 0, 0)

            ################### sleep class
            immatrix = []
            immatrix.append(self.A)
            immatrix = np.asarray(immatrix)
            immatrix = immatrix.astype('float32', copy=False)
            immatrix /= 4
            model_sleep = load_model('class sleep model.h5')
            model_sleep.summary()
            predict_sleep = model_sleep.predict(immatrix, verbose=1)
            final_predict_sleep = np.argmax(predict_sleep, axis=1)
            if final_predict_sleep == 0:
                temp = arabic_reshaper.reshape(
                    "2 ـ ورزشکار گرامی باید میزان خواب کافی را در شبانه روز در اولویت قرار دهید.")
                temp_text = get_display(temp)
                self.l1.text = temp_text
            if final_predict_sleep == 1:
                temp = arabic_reshaper.reshape(
                    "2 ـ ورزشکار گرامی سطح خواب شما در شبانه روز در حد متوسط است و باید مقداری ساعات خواب خود را افزایش دهید.")
                temp_text = get_display(temp)
                self.l1.text = temp_text
            if final_predict_sleep == 2:
                temp = arabic_reshaper.reshape("2 ـ ورزشکار گرامی سطح خواب شما عالی است.")
                temp_text = get_display(temp)
                self.l1.text = temp_text

            ################### geography class
            immatrix = []
            immatrix.append(self.A)
            immatrix = np.asarray(immatrix)
            immatrix = immatrix.astype('float32', copy=False)
            immatrix /= 4
            model = load_model('geography class model.h5')
            model.summary()
            predict = model.predict(immatrix, verbose=1)
            final_predict = np.argmax(predict, axis=1)
            if final_predict == 0:
                temp = arabic_reshaper.reshape(
                    "1 ـ ورزشکار گرامی موقعیت جغرافیایی (آب و هوا، طبیعت و ...) به شدت در روحیه و بازدهی تمرین شما اثر گذار است.")
                temp_text = get_display(temp)
                self.l2.text = temp_text
            if final_predict == 1:
                temp = arabic_reshaper.reshape(
                    "1 ـ ورزشکار گرامی موقعیت جغرافیایی (آب و هوا، طبیعت و ...) تاثیر نسبی در روحیه و بازدهی تمرین شما اثر گذار است.")
                temp_text = get_display(temp)
                self.l2.text = temp_text
            if final_predict == 2:
                temp = arabic_reshaper.reshape(
                    "1 ـ ورزشکار گرامی موقعیت جغرافیایی (آب و هوا، طبیعت و ...) تاثیری در روحیه و بازدهی تمرین شما ندارد.")
                temp_text = get_display(temp)
                self.l2.text = temp_text

            ################### parallel class
            immatrix = []
            immatrix.append(self.A)
            immatrix = np.asarray(immatrix)
            immatrix = immatrix.astype('float32', copy=False)
            immatrix /= 4
            model = load_model('parallel class model.h5')
            model.summary()
            predict = model.predict(immatrix, verbose=1)
            final_predict = np.argmax(predict, axis=1)
            if final_predict == 0:
                temp = arabic_reshaper.reshape(
                    "3 ـ ورزشکار گرامی شما از رشته های موازی ورزشی استفاده ای نمی کنید.")
                temp_text = get_display(temp)
                self.l3.text = temp_text
            if final_predict == 1:
                temp = arabic_reshaper.reshape(
                    "3 ـ ورزشکار گرامی شما به طور نسبی از رشته های موازی ورزشی استفاده می کنید.")
                temp_text = get_display(temp)
                self.l3.text = temp_text
            if final_predict == 2:
                temp = arabic_reshaper.reshape(
                    "3 ـ ورزشکار گرامی شما از رشته های موازی ورزشی به خوبی بهره می برید.")
                temp_text = get_display(temp)
                self.l3.text = temp_text

            ################### technology class
            immatrix = []
            immatrix.append(self.A)
            immatrix = np.asarray(immatrix)
            immatrix = immatrix.astype('float32', copy=False)
            immatrix /= 4
            model = load_model('technology class model.h5')
            model.summary()
            predict = model.predict(immatrix, verbose=1)
            final_predict = np.argmax(predict, axis=1)
            if final_predict == 0:
                temp = arabic_reshaper.reshape(
                    "4 ـ ورزشکار گرامی شما از تکنولوژی جدید ورزشی بهره ای نمی برید. ")
                temp_text = get_display(temp)
                self.l4.text = temp_text
            if final_predict == 1:
                temp = arabic_reshaper.reshape(
                    "4 ـ ورزشکار گرامی شما از تکنولوژی جدید ورزشی به طور نسبی استفاده می کنید. ")
                temp_text = get_display(temp)
                self.l4.text = temp_text
            if final_predict == 2:
                temp = arabic_reshaper.reshape(
                    "4 ـ ورزشکار گرامی شما از تکنولوژی جدید ورزشی بهره به خوبی بهره می برید. ")
                temp_text = get_display(temp)
                self.l4.text = temp_text

            ################### time of exercise
            immatrix = []
            immatrix.append(self.A)
            immatrix = np.asarray(immatrix)
            immatrix = immatrix.astype('float32', copy=False)
            immatrix /= 4
            model = load_model('time of exercise model.h5')
            model.summary()
            predict = model.predict(immatrix, verbose=1)
            final_predict = np.argmax(predict, axis=1)
            if final_predict == 0:
                temp = arabic_reshaper.reshape(
                    "5 ـ ورزشکار گرامی شما تمایل دارید که صبح ها ورزش کنید.")
                temp_text = get_display(temp)
                self.l5.text = temp_text
            if final_predict == 1:
                temp = arabic_reshaper.reshape(
                    "5 ـ ورزشکار گرامی شما تمایل دارید که در بعد از ظهر ورزش کنید و لازم است که صبح ورزش کنید.")
                temp_text = get_display(temp)
                self.l5.text = temp_text
            if final_predict == 2:
                temp = arabic_reshaper.reshape(
                    "5 ـ ورزشکار گرامی برای شما اهمیتی ندارد که صبح ها یا بعد از ظهر ها ورزش کنید. ولی توصیه می شود که صبح ها ورزش کنید. ")
                temp_text = get_display(temp)
                self.l5.text = temp_text

    #دکمه همیشه #######
    def always(self,instance):
        global count
        if count != 57:
            self.A.append(4)
            print("len A:", len(self.A))
            # global count
            count = count + 1
            print("count:", count)
            if count != 57:
                temp = arabic_reshaper.reshape(Questions[count])
                print("question number:", temp)
                temp_text = get_display(temp)
                print("temp_text:", temp_text)
                self.l1.text = temp_text

        if count == 49:
            temp = arabic_reshaper.reshape("بر اساس میزان کالری و انرژی")
            temp_text = get_display(temp)
            self.b1.text = temp_text
            temp = arabic_reshaper.reshape("بر حسب تعداد وعده")
            temp_text = get_display(temp)
            self.b2.text = temp_text
            temp = arabic_reshaper.reshape("به تناسب ذائقه و میل")
            temp_text = get_display(temp)
            self.b3.text = temp_text
            temp = arabic_reshaper.reshape("به تناسب هزینه")
            temp_text = get_display(temp)
            self.b4.text = temp_text
            temp = arabic_reshaper.reshape("تمام موارد")
            temp_text = get_display(temp)
            self.b5.text = temp_text
            self.b4.disabled = False
            self.b5.disabled = False

        if (count == 51 or count == 53 or count == 55):
            temp = arabic_reshaper.reshape("هرگز")
            temp_text = get_display(temp)
            self.b1.text = temp_text
            temp = arabic_reshaper.reshape("به ندرت")
            temp_text = get_display(temp)
            self.b2.text = temp_text
            temp = arabic_reshaper.reshape("گاهی")
            temp_text = get_display(temp)
            self.b3.text = temp_text
            temp = arabic_reshaper.reshape("اغلب")
            temp_text = get_display(temp)
            self.b4.text = temp_text
            self.b4.background_color = usually_color
            always_text = arabic_reshaper.reshape("همیشه")
            always_text_persian = get_display(always_text)
            self.b5.text = always_text_persian
            self.b5.background_color = always_color
            self.b5.disabled = False
            self.b4.disabled = False

        if count == 50:
            temp = arabic_reshaper.reshape("با توجه به فعالیت و کار روزانه")
            temp_text = get_display(temp)
            self.b1.text = temp_text
            temp = arabic_reshaper.reshape("هشت تا 12 لیوان در روز")
            temp_text = get_display(temp)
            self.b2.text = temp_text
            temp = arabic_reshaper.reshape("شدت و زمان ورزش")
            temp_text = get_display(temp)
            self.b3.text = temp_text
            temp = arabic_reshaper.reshape("تمام موارد")
            temp_text = get_display(temp)
            self.b4.text = temp_text
            self.b4.disabled = False
            self.b5.disabled = True
            self.b5.text = ""
            self.b5.background_color = (0, 0, 0, 0)

        if count == 52:
            temp = arabic_reshaper.reshape("هر ماه یکبار")
            temp_text = get_display(temp)
            self.b1.text = temp_text
            temp = arabic_reshaper.reshape("هر سه ماه یکبار")
            temp_text = get_display(temp)
            self.b2.text = temp_text
            temp = arabic_reshaper.reshape("هر شش ماه یکبار")
            temp_text = get_display(temp)
            self.b3.text = temp_text
            temp = arabic_reshaper.reshape("با مشورت پزشک متخصص")
            temp_text = get_display(temp)
            self.b4.text = temp_text
            self.b4.disabled = False
            self.b5.disabled = True
            self.b5.text = ""
            self.b5.background_color = (0, 0, 0, 0)

        if count == 54:
            temp = arabic_reshaper.reshape("تمرین فردی")
            temp_text = get_display(temp)
            self.b1.text = temp_text
            temp = arabic_reshaper.reshape("تمرین های دونفره")
            temp_text = get_display(temp)
            self.b2.text = temp_text
            temp = arabic_reshaper.reshape("تمرین های گروهی")
            temp_text = get_display(temp)
            self.b3.text = temp_text
            self.b4.disabled = True
            self.b4.text = ""
            self.b4.background_color = (0, 0, 0, 0)
            self.b5.disabled = True
            self.b5.text = ""
            self.b5.background_color = (0, 0, 0, 0)

        if count == 56:
            temp = arabic_reshaper.reshape("کشف ذوق، علاقه و استعداد فردی")
            temp_text = get_display(temp)
            self.b1.text = temp_text
            self.b1.font_size="25sp"
            temp = arabic_reshaper.reshape("امکانات و همه گیری در سطح شهر یا کشور")
            temp_text = get_display(temp)
            self.b2.text = temp_text
            self.b2.font_size="25sp"
            temp = arabic_reshaper.reshape("موفقیت و نام آوری بزرگان، خانواده یا فامیل")
            temp_text = get_display(temp)
            self.b3.text = temp_text
            self.b3.font_size="25sp"
            temp = arabic_reshaper.reshape("میزان هزینه")
            temp_text = get_display(temp)
            self.b4.text = temp_text
            self.b4.font_size="30sp"
            self.b4.background_color = usually_color
            self.b4.disabled = False
            self.b5.disabled = True
            self.b5.text = ""
            self.b5.background_color = (0, 0, 0, 0)

        if count == 57:
            self.b1.disabled = True
            self.b1.text = ""
            self.b1.background_color = (0, 0, 0, 0)
            self.b2.disabled = True
            self.b2.text = ""
            self.b2.background_color = (0, 0, 0, 0)
            self.b3.disabled = True
            self.b3.text = ""
            self.b3.background_color = (0, 0, 0, 0)
            self.b4.disabled = True
            self.b4.text = ""
            self.b4.background_color = (0, 0, 0, 0)
            self.b5.disabled = True
            self.b5.text = ""
            self.b5.background_color = (0, 0, 0, 0)

            ################### sleep class
            immatrix = []
            immatrix.append(self.A)
            immatrix = np.asarray(immatrix)
            immatrix = immatrix.astype('float32', copy=False)
            immatrix /= 4
            model_sleep = load_model('class sleep model.h5')
            model_sleep.summary()
            predict_sleep = model_sleep.predict(immatrix, verbose=1)
            final_predict_sleep = np.argmax(predict_sleep, axis=1)
            if final_predict_sleep == 0:
                temp = arabic_reshaper.reshape(
                    "2 ـ ورزشکار گرامی باید میزان خواب کافی را در شبانه روز در اولویت قرار دهید.")
                temp_text = get_display(temp)
                self.l1.text = temp_text
            if final_predict_sleep == 1:
                temp = arabic_reshaper.reshape(
                    "2 ـ ورزشکار گرامی سطح خواب شما در شبانه روز در حد متوسط است و باید مقداری ساعات خواب خود را افزایش دهید.")
                temp_text = get_display(temp)
                self.l1.text = temp_text
            if final_predict_sleep == 2:
                temp = arabic_reshaper.reshape("2 ـ ورزشکار گرامی سطح خواب شما عالی است.")
                temp_text = get_display(temp)
                self.l1.text = temp_text

            ################### geography class
            immatrix = []
            immatrix.append(self.A)
            immatrix = np.asarray(immatrix)
            immatrix = immatrix.astype('float32', copy=False)
            immatrix /= 4
            model = load_model('geography class model.h5')
            model.summary()
            predict = model.predict(immatrix, verbose=1)
            final_predict = np.argmax(predict, axis=1)
            if final_predict == 0:
                temp = arabic_reshaper.reshape(
                    "1 ـ ورزشکار گرامی موقعیت جغرافیایی (آب و هوا، طبیعت و ...) به شدت در روحیه و بازدهی تمرین شما اثر گذار است.")
                temp_text = get_display(temp)
                self.l2.text = temp_text
            if final_predict == 1:
                temp = arabic_reshaper.reshape(
                    "1 ـ ورزشکار گرامی موقعیت جغرافیایی (آب و هوا، طبیعت و ...) تاثیر نسبی در روحیه و بازدهی تمرین شما اثر گذار است.")
                temp_text = get_display(temp)
                self.l2.text = temp_text
            if final_predict == 2:
                temp = arabic_reshaper.reshape(
                    "1 ـ ورزشکار گرامی موقعیت جغرافیایی (آب و هوا، طبیعت و ...) تاثیری در روحیه و بازدهی تمرین شما ندارد.")
                temp_text = get_display(temp)
                self.l2.text = temp_text

            ################### parallel class
            immatrix = []
            immatrix.append(self.A)
            immatrix = np.asarray(immatrix)
            immatrix = immatrix.astype('float32', copy=False)
            immatrix /= 4
            model = load_model('parallel class model.h5')
            model.summary()
            predict = model.predict(immatrix, verbose=1)
            final_predict = np.argmax(predict, axis=1)
            if final_predict == 0:
                temp = arabic_reshaper.reshape(
                    "3 ـ ورزشکار گرامی شما از رشته های موازی ورزشی استفاده ای نمی کنید.")
                temp_text = get_display(temp)
                self.l3.text = temp_text
            if final_predict == 1:
                temp = arabic_reshaper.reshape(
                    "3 ـ ورزشکار گرامی شما به طور نسبی از رشته های موازی ورزشی استفاده می کنید.")
                temp_text = get_display(temp)
                self.l3.text = temp_text
            if final_predict == 2:
                temp = arabic_reshaper.reshape(
                    "3 ـ ورزشکار گرامی شما از رشته های موازی ورزشی به خوبی بهره می برید.")
                temp_text = get_display(temp)
                self.l3.text = temp_text

            ################### technology class
            immatrix = []
            immatrix.append(self.A)
            immatrix = np.asarray(immatrix)
            immatrix = immatrix.astype('float32', copy=False)
            immatrix /= 4
            model = load_model('technology class model.h5')
            model.summary()
            predict = model.predict(immatrix, verbose=1)
            final_predict = np.argmax(predict, axis=1)
            if final_predict == 0:
                temp = arabic_reshaper.reshape(
                    "4 ـ ورزشکار گرامی شما از تکنولوژی جدید ورزشی بهره ای نمی برید. ")
                temp_text = get_display(temp)
                self.l4.text = temp_text
            if final_predict == 1:
                temp = arabic_reshaper.reshape(
                    "4 ـ ورزشکار گرامی شما از تکنولوژی جدید ورزشی به طور نسبی استفاده می کنید. ")
                temp_text = get_display(temp)
                self.l4.text = temp_text
            if final_predict == 2:
                temp = arabic_reshaper.reshape(
                    "4 ـ ورزشکار گرامی شما از تکنولوژی جدید ورزشی بهره به خوبی بهره می برید. ")
                temp_text = get_display(temp)
                self.l4.text = temp_text

            ################### time of exercise
            immatrix = []
            immatrix.append(self.A)
            immatrix = np.asarray(immatrix)
            immatrix = immatrix.astype('float32', copy=False)
            immatrix /= 4
            model = load_model('time of exercise model.h5')
            model.summary()
            predict = model.predict(immatrix, verbose=1)
            final_predict = np.argmax(predict, axis=1)
            if final_predict == 0:
                temp = arabic_reshaper.reshape(
                    "5 ـ ورزشکار گرامی شما تمایل دارید که صبح ها ورزش کنید.")
                temp_text = get_display(temp)
                self.l5.text = temp_text
            if final_predict == 1:
                temp = arabic_reshaper.reshape(
                    "5 ـ ورزشکار گرامی شما تمایل دارید که در بعد از ظهر ورزش کنید و لازم است که صبح ورزش کنید.")
                temp_text = get_display(temp)
                self.l5.text = temp_text
            if final_predict == 2:
                temp = arabic_reshaper.reshape(
                    "5 ـ ورزشکار گرامی برای شما اهمیتی ندارد که صبح ها یا بعد از ظهر ها ورزش کنید. ولی توصیه می شود که صبح ها ورزش کنید. ")
                temp_text = get_display(temp)
                self.l5.text = temp_text

    #دکمه ادامه #######
    def continue_func(self,instance):

        print("count:", count)
        temp = arabic_reshaper.reshape(Questions[count])
        print("question number:", temp)
        temp_text = get_display(temp)
        print("temp_text:", temp_text)


        self.l1.text = temp_text
        print("l1.text:", self.l1.text)
        self.b0.disabled = True
        self.b0.background_color = (0, 0, 0, 0)
        self.b0.text = ""

        self.r.add_widget(self.l2)
        self.r.add_widget(self.l3)
        self.r.add_widget(self.l4)
        self.r.add_widget(self.l5)
        self.r.add_widget(self.b1)
        self.r.add_widget(self.b2)
        self.r.add_widget(self.b3)
        self.r.add_widget(self.b4)
        self.r.add_widget(self.b5)





    def build(self):


        print("count:", count)
        temp = arabic_reshaper.reshape(start_statement)
        print("question number:", temp)
        temp_text = get_display(temp)
        print("temp_text:", temp_text)

        self.r = RelativeLayout()



        self.l1 = Label(font_name="C:\Windows\Fonts/BNAZANIN.TTF", font_size="50sp", markup=True,
                       pos_hint={'x': 0, 'y': 0.3})
        self.l1.text = temp_text
        print("l1.text:",self.l1.text)


        self.l2 = Label(font_name="BNAZANIN.TTF", font_size="50sp", markup=True,
                        pos_hint={'x': 0, 'y': 0.4})

        self.l3 = Label(font_name="BNAZANIN.TTF", font_size="50sp", markup=True,
                        pos_hint={'x': 0, 'y': 0.2})

        self.l4 = Label(font_name="BNAZANIN.TTF", font_size="50sp", markup=True,
                        pos_hint={'x': 0, 'y': 0.1})

        self.l5 = Label(font_name="BNAZANIN.TTF", font_size="50sp", markup=True,
                        pos_hint={'x': 0, 'y': 0})

        continue_text = arabic_reshaper.reshape("ادامه")
        continue_text_persian = get_display(continue_text)
        self.b0 = Button(size_hint=(.2, .2), pos_hint={'x': 0.4, 'y': 0.2}, text=continue_text_persian,
                         font_name="BNAZANIN.TTF", font_size="50sp", background_color=(1,0,1,1),
                         on_press=self.continue_func)


        never_text = arabic_reshaper.reshape("هرگز")
        never_text_persian = get_display(never_text)
        self.b1 = Button(size_hint=(.2, .2), pos_hint={'x': 0, 'y': 0}, text=never_text_persian,
                    font_name="BNAZANIN.TTF", font_size="40sp", background_color=never_color,on_press=self.never)
        # b1.bind(on_press=never)


        rarely_text = arabic_reshaper.reshape("به ندرت")
        rarely_text_persian = get_display(rarely_text)
        self.b2 = Button(size_hint=(.2, .2), pos_hint={'x': 0.2, 'y': 0}, text=rarely_text_persian,
                    font_name="BNAZANIN.TTF", font_size="40sp", background_color=rarely_color,on_press=self.rarely)
        # b2.bind(on_press=rarely)


        sometimes_text = arabic_reshaper.reshape("گاهی")
        sometimes_text_persian = get_display(sometimes_text)
        self.b3 = Button(size_hint=(.2, .2), pos_hint={'x': .4, 'y': 0}, text=sometimes_text_persian,
                    font_name="BNAZANIN.TTF", font_size="40sp", background_color=sometimes_color,on_press=self.sometimes)
        # b3.bind(on_press=sometimes)


        usually_text = arabic_reshaper.reshape("اغلب")
        usually_text_persian = get_display(usually_text)
        self.b4 = Button(size_hint=(.2, .2), pos_hint={'x': 0.6, 'y': 0}, text=usually_text_persian,
                    font_name="BNAZANIN.TTF", font_size="40sp", background_color=usually_color,on_press=self.usually)
        # b4.bind(on_press=usually)


        always_text = arabic_reshaper.reshape("همیشه")
        always_text_persian = get_display(always_text)
        self.b5 = Button(size_hint=(.2, .2), pos_hint={'x': 0.8, 'y': 0}, text=always_text_persian,
                    font_name="BNAZANIN.TTF", font_size="40sp", background_color=always_color,on_press= self.always)
        # b5.bind(on_press=always)

        # self.img_cism = Image(source='cism.png')
        # self.img_cism.allow_stretch = False
        # self.img_cism.keep_ratio = False
        # self.img_cism.size_hint_x = 0.15
        # self.img_cism.size_hint_y = 0.15
        # self.img_cism.pos_hint = {'x': 0.8, 'y': 0.7}
        # self.img_cism.opacity = 1
        #
        # self.img_force = Image(source='force.png')
        # self.img_force.allow_stretch = False
        # self.img_force.keep_ratio = False
        # self.img_force.size_hint_x = 0.15
        # self.img_force.size_hint_y = 0.15
        # self.img_force.pos_hint = {'x': 0 , 'y': 0.7}
        # self.img_force.opacity = 1
        #
        # self.img_back = Image(source='back2.jpg')
        # self.img_back.allow_stretch = True
        # self.img_back.keep_ratio = True
        # # self.img_back.height = "100sp"
        # # self.img_back.width = "100dp"
        # self.img_back.size_hint_x = 1.6
        # self.img_back.size_hint_y = 2

        self.img_back = Image(source='new2.jpg')
        self.img_back.allow_stretch = False
        self.img_back.keep_ratio = False
        # self.img_back.height = "100sp"
        # self.img_back.width = "100dp"
        self.img_back.size_hint_x = 1.1
        self.img_back.size_hint_y = 1.1
        self.img_back.pos_hint = {'x': 0, 'y': 0}




        self.r.add_widget(self.img_back)
        # self.r.add_widget(self.img_cism)
        # self.r.add_widget(self.img_force)
        self.r.add_widget(self.b0)
        self.r.add_widget(self.l1)
        # self.r.add_widget(self.l2)
        # self.r.add_widget(self.l3)
        # self.r.add_widget(self.l4)
        # self.r.add_widget(self.l5)
        # self.r.add_widget(self.b1)
        # self.r.add_widget(self.b2)
        # self.r.add_widget(self.b3)
        # self.r.add_widget(self.b4)
        # self.r.add_widget(self.b5)





        return self.r





######################################################################################################


Relative_Layout_1().run()



