import smtplib
import imghdr
from email.message import EmailMessage 

app_pass = ""
host_user= "uni.ras.ieee@gmail.com"

smtp =smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp.login(host_user, app_pass)

with open('Genji.jpg', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg = EmailMessage()
msg['Subject'] = "SEMANA STARTUP!!"
msg['From'] = host_user
msg['To'] = host_user
msg.set_content("Are you available for lunch today?")
# msg.add_attachment(file_data, maintype ="image",
#                     subtype=file_type,
#                     filename= file_name)
msg.add_alternative(""" \n\n
<!DOCTYPE html>
<html xmlns:o=3D"urn:schemas-microsoft-com:office:office" xmlns:v=3D"urn:sc=
hemas-microsoft-com:vml"><head>
<!--[if !mso]><!-- -->
<link href=3D"https://fonts.googleapis.com/css?family=3DOpen+Sans:300,400,7=
00" rel=3D"stylesheet"/>
<!--<![endif]--> <!--[if gte mso 9]><xml>
 <o:OfficeDocumentSettings>
   <o:AllowPNG/>
   <o:PixelsPerInch>96</o:PixelsPerInch>
 </o:OfficeDocumentSettings>
</xml><![endif]-->


<!-- MITSLoanManagement_CustomFrame_TL_August302017 -->
<!-- dupe rev w/ header and footer removed by MH 9/28/17 -->


<style type=3D"text/css">
@media screen and (max-width: 480px) {
    #block_tekxnuxs .e2ma-holder.e2ma-follow-holder table, #block_apufgmzz =
.e2ma-holder.e2ma-follow-holder table, #block_zewqpmke .e2ma-holder.e2ma-fo=
llow-holder table {
        width: auto !important;
        margin: 0 auto
        }
    #block_zewqpmke .e2ma-holder.e2ma-follow-holder table td, #block_apufgm=
zz .e2ma-holder.e2ma-follow-holder table td, #block_tekxnuxs .e2ma-holder.e=
2ma-follow-holder table td {
        display: table-cell !important;
        float: none !important;
        width: auto !important;
        padding-left: 2px !important;
        padding-right: 2px !important
        }
    .e2ma-combo-button, .e2ma-template .mobile-width-nopad {
        width: 100% !important
        }
    .e2ma-template html {
        -webkit-text-size-adjust: none
        }
    .e2ma-template .e2ma-combo-content li, .e2ma-template .e2ma-content-blo=
ck div.e2ma-p-div, .e2ma-template .e2ma-combo-block li, .e2ma-template .e2m=
a-content-block li, .e2ma-template .e2ma-combo-block div.e2ma-p-div, .e2ma-=
template .e2ma-combo-content div.e2ma-p-div {
        font-size: 16px !important
        }
    .e2ma-template .e2ma-holder table, .e2ma-template .e2ma-holder table td=
 {
        display: table !important;
        float: none !important;
        width: 100% !important;
        padding-left: 0 !important;
        padding-right: 0 !important
        }
    .e2ma-template .e2ma-single-column-layout table {
        float: none !important;
        margin: 0 auto
        }
    .e2ma-template .e2ma-unsubscribe span {
        font-size: 12px !important
        }
    .e2ma-template .social-sharing {
        text-align: center !important;
        padding-bottom: 10px
        }
    .e2ma-template .scale img, .e2ma-template .e2ma-layout-column-content i=
mg, .e2ma-template .e2ma-layout-column-sidebar img, .e2ma-template .e2ma-si=
ngle-column-layout img, .e2ma-template .editable_image img, .e2ma-template =
.e2ma-layout-column-sidebar-2 img, .e2ma-template .e2ma-layout-column-sideb=
ar-3 img {
        max-width: 100%;
        height: auto;
        margin: 0 auto
        }
    .e2ma-template .footer-social img {
        width: 44px !important;
        height: 43px !important;
        margin: 0 auto
        }
    .e2ma-template .share-block {
        text-align: center !important;
        margin: 0 auto !important
        }
    .e2ma-template .footer-text {
        text-align: center !important
        }
    .e2ma-template .mobile-width {
        width: 100% !important;
        padding-left: 10px;
        padding-right: 10px
        }
    .e2ma-template .stack, .e2ma-template .e2ma-layout-column-sidebar-3, .e=
2ma-template .e2ma-layout-column-content, .e2ma-template .e2ma-layout-colum=
n-sidebar, .e2ma-template .e2ma-layout-column-sidebar-2 {
        display: block !important;
        width: 100% !important
        }
    .e2ma-template .hide {
        display: none !important
        }
    .e2ma-template .center img, .e2ma-template .center {
        text-align: center !important;
        margin: 0 auto
        }
    .e2ma-template .scale-up img {
        width: 100%;
        height: auto;
        margin: 0 auto
        }
    .e2ma-template .addpad {
        padding: 10px 0 !important
        }
    .e2ma-template .addpad-top {
        padding-top: 10px !important
        }
    .e2ma-template .sanpad {
        padding: 0 !important
        }
    .e2ma-template .sanborder {
        border: none !important
        }
    .e2ma-template .footerlinks {
        color: #6b6c6e;
        text-decoration: none
        }
    }
.e2ma-template h1, .e2ma-template h2, .e2ma-template h3, .e2ma-template h4,=
 .e2ma-template h5, .e2ma-template h6 {
    margin: 0;
    padding: 0;
    border: 0;
    font-size: 100%;
    font: inherit;
    vertical-align: baseline
    }
.e2ma-template h1 {
    font-family: "Open Sans", Helvetica, sans-serif;
    font-size: 24px;
    font-weight: 300;
    color: #333
    }
.e2ma-template h2 {
    font-family: "Open Sans", Helvetica, sans-serif;
    font-size: 18px;
    font-weight: 400;
    color: #333
    }
.e2ma-template h3 {
    font-family: "Open Sans", Helvetica, sans-serif;
    font-size: 15px;
    font-weight: 700;
    color: #333
    }
.e2ma-template h4 {
    font-family: "Open Sans", Helvetica, sans-serif;
    font-size: 22px;
    font-weight: 700;
    color: #333
    }
.e2ma-template .e2ma-content-block div.e2ma-p-div, .e2ma-template .e2ma-com=
bo-block div.e2ma-p-div, .e2ma-template .e2ma-combo-content div.e2ma-p-div,=
 .e2ma-template .e2ma-content-block li, .e2ma-template .e2ma-combo-block li=
, .e2ma-template .e2ma-combo-content li {
    font-family: "Open Sans", Helvetica, sans-serif;
    font-size: 14px;
    color: #333
    }
.e2ma-template #template_container a, .e2ma-template .link {
    color: #333;
    text-decoration: none
    }
.e2ma-template #template_footer a, .e2ma-template .link {
    color: #6b6c6e;
    text-decoration: none
    }
.e2ma-template blockquote {
    padding-top: 10px;
    padding-bottom: 10px;
    border-top: 1px solid #000;
    border-bottom: 1px solid #000;
    font-style: italic
    }
.e2ma-template blockquote div.e2ma-p-div {
    margin-bottom: 0
    }
.e2ma-template .editable_image img {
    display: block;
    border: 0
    }
.e2ma-template .e2ma-unsubscribe {
    padding-bottom: 10px
    }
</style><meta content=3D"telephone=3Dno" name=3D"format-detection"/><meta c=
ontent=3D"telephone=3Dno" name=3D"format-detection"/></head><body class=3D"=
e2ma-template" style=3D"margin:0; padding:0; width:100% !important; backgro=
und-color: #e9e9e9">

<div style=3D"display: none !important; mso-hide:all;">Actionable insights,=
 for as low as $1.09 per week.</div>
<img style=3D"display: none !important; mso-hide:all;" src=3D"https://image=
s.e2ma.net/images/spacer.gif" width=3D"1" height=3D"1" alt=3D"Actionable in=
sights, for as low as $1.09 per week.">





<div style=3D"margin:0; padding:0; width:100% !important; background-color:=
 #e9e9e9">
<table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" data-e2ma-color=3D"=
#e9e9e9, #333332, #a41e27, #ed1a36, #555656;" style=3D"font-family: Arial, =
Helvetica, sans-serif;font-size: 12px" width=3D"100%">
<tbody>
<tr>
<td align=3D"center" class=3D"sanpad" valign=3D"top">
<table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" class=3D"mobile-wid=
th-nopad" id=3D"template_container" style=3D"font-family: Arial, Helvetica,=
 sans-serif;font-size: 12px;width:640px">
<tbody>
<tr>
<td align=3D"left" valign=3D"top">
<table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" style=3D"font-famil=
y: Arial, Helvetica, sans-serif;font-size: 12px" width=3D"100%">
<tbody>
<tr>
<td align=3D"left" style=3D"background-color:#ffffff" valign=3D"top"><table=
 border=3D"0" cellpadding=3D"0" cellspacing=3D"0" class=3D"e2ma-row-region-=
content e2ma-section" style=3D"font-family: Arial, Helvetica, sans-serif;fo=
nt-size: 12px" width=3D"100%"><tbody><tr><td class=3D"e2ma-layout-column-co=
ntent">
<table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" class=3D"e2ma-block=
-outer" id=3D"block_tekxnuxs" style=3D"font-family: Arial, Helvetica, sans-=
serif;font-size: 12px" width=3D"100%"> <tbody><tr> <td class=3D"e2ma-wrappe=
r" style=3D"padding-right: 0;padding-bottom: 0;padding-left: 0" valign=3D"t=
op"> <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" style=3D"font-=
family: Arial, Helvetica, sans-serif;font-size: 12px" width=3D"100%"> <tbod=
y><tr> <td class=3D"e2ma-holder" style=3D"padding: 10px 0 0 0;background-co=
lor: #292929" valign=3D"top"> <table border=3D"0" cellpadding=3D"0" cellspa=
cing=3D"0" style=3D"font-family: Arial, Helvetica, sans-serif;font-size: 12=
px"> <tbody><tr><td valign=3D"top"><table border=3D"0" cellpadding=3D"0" ce=
llspacing=3D"0" style=3D"font-family: Arial, Helvetica, sans-serif;font-siz=
e: 12px"><tbody><tr> <td class=3D"e2ma-image-td" style=3D"text-align: cente=
r; padding: 10px 260px 10px 260px; " valign=3D"top"> <a href=3D"https://t.e=
2ma.net/click/bv2h2w/r3z1rkkb/zd9lwpj" style=3D"font-weight: normal;font-we=
ight: normal;color: #333;text-decoration: none;color: #333;text-decoration:=
 none" target=3D"_blank"> <img alt=3D"MIT Sloan Management Review" border=
=3D"0" height=3D"34" src=3D"https://d31hzlhk6di2h5.cloudfront.net/20220407/=
5a/9d/41/19/3d9d4a175310a7eab7c272b9_240x68.png" style=3D"display: block" w=
idth=3D"120"/> </a> </td> </tr></tbody></table></td></tr> </tbody></table> =
</td> </tr> </tbody></table> </td> </tr> </tbody></table>
</td></tr></tbody></table> <div class=3D"e2ma-single-column-layout e2ma-sec=
tion"><table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" style=3D"font=
-family: Arial, Helvetica, sans-serif;font-size: 12px" width=3D"100%"><tbod=
y><tr><td class=3D"e2ma-design-option-template" data-e2ma-styles=3D"backgro=
und, border-left, border-right" style=3D"background-color: transparent">
<table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" class=3D"e2ma-block=
-outer" id=3D"block_apufgmzz" style=3D"font-family: Arial, Helvetica, sans-=
serif;font-size: 12px" width=3D"100%"> <tbody><tr> <td class=3D"e2ma-wrappe=
r" style=3D"padding-right: 0;padding-bottom: 0;padding-left: 0" valign=3D"t=
op"> <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" style=3D"font-=
family: Arial, Helvetica, sans-serif;font-size: 12px" width=3D"100%"> <tbod=
y><tr> <td class=3D"e2ma-holder" style=3D"padding: 0;background-color: tran=
sparent" valign=3D"top"> <table border=3D"0" cellpadding=3D"0" cellspacing=
=3D"0" style=3D"font-family: Arial, Helvetica, sans-serif;font-size: 12px">=
 <tbody><tr><td valign=3D"top"><table border=3D"0" cellpadding=3D"0" cellsp=
acing=3D"0" style=3D"font-family: Arial, Helvetica, sans-serif;font-size: 1=
2px"><tbody><tr> <td class=3D"e2ma-image-td" style=3D"text-align: center; p=
adding: 0px 0px 0px 0px; " valign=3D"top"> <a href=3D"https://t.e2ma.net/cl=
ick/bv2h2w/r3z1rkkb/f69lwpj" style=3D"font-weight: normal;font-weight: norm=
al;color: #333;text-decoration: none;color: #333;text-decoration: none" tar=
get=3D"_blank"> <img alt=3D"Get the insights you need to be an innovative l=
eader. Invest in your career for as low as $1.09 per week." border=3D"0" he=
ight=3D"583" src=3D"https://d31hzlhk6di2h5.cloudfront.net/20220407/ee/46/cf=
/55/6c22b15adde5a88d7dbd6861_1280x1166.jpg" style=3D"display: block" width=
=3D"640"/> </a> </td> </tr></tbody></table></td></tr> </tbody></table> </td=
> </tr> </tbody></table> </td> </tr> </tbody></table>
<table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" class=3D"e2ma-block=
-outer e2ma-button" id=3D"block_nkuxbgnm" style=3D"font-family: Arial, Helv=
etica, sans-serif;font-size: 12px" width=3D"100%"> <tbody><tr> <td class=3D=
"e2ma-wrapper" style=3D"padding-right: 0;padding-bottom: 0;padding-left: 0"=
 valign=3D"top"> <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" cl=
ass=3D"e2ma-holder" style=3D"font-family: Arial, Helvetica, sans-serif;font=
-size: 12px;padding: 20px 40px 20px 40px;background-color: transparent" wid=
th=3D"100%"> <tbody><tr> <td align=3D"center"> <table class=3D"c-collapsed-=
table" style=3D"font-family: Arial, Helvetica, sans-serif;font-size: 12px;b=
order-spacing: 0"> <tbody><tr> <td bgcolor=3D"#ed1a36" style=3D"-webkit-bor=
der-radius: 0px; -moz-border-radius: 0px; border-radius: 0px; box-sizing: b=
order-box; "> <a href=3D"https://t.e2ma.net/click/bv2h2w/r3z1rkkb/vyamwpj" =
style=3D"font-weight: normal;font-weight: normal;color: #333;text-decoratio=
n: none;color: #333;text-decoration: none; padding: 16px 22px; font-size: 1=
8px; font-family: Arial, Helvetica, sans-serif; color: #ffffff; text-align:=
 center; text-decoration: none; border-radius: 0px; -webkit-border-radius: =
0px; -moz-border-radius: 0px; background-color: #ed1a36; font-style: normal=
; font-weight: bold; display: block; border: 1px solid #ed1a36; mso-line-he=
ight-rule: exactly; line-height:110%">Learn more =C2=BB</a> </td> </tr> </t=
body></table> </td> </tr> </tbody></table> </td> </tr> </tbody></table>
<table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" class=3D"e2ma-block=
-outer" id=3D"block_kglpspoi" style=3D"font-family: Arial, Helvetica, sans-=
serif;font-size: 12px" width=3D"100%"> <tbody><tr> <td style=3D"padding-bot=
tom:20px"></td> </tr> <tr> <td class=3D"e2ma-wrapper e2ma-image-td" style=
=3D"padding-right: 40px;padding-bottom: 20px;padding-left: 40px;font-size: =
12px;line-height: 1.5" valign=3D"top"> <table border=3D"0" cellpadding=3D"0=
" cellspacing=3D"0" style=3D"font-family: Arial, Helvetica, sans-serif;font=
-size: 12px" width=3D"100%"> <tbody><tr> <td class=3D"e2ma-holder" style=3D=
"padding: 20px 40px 20px 40px;background-color: transparent;border-width: 1=
px;border-style: solid;border-color: #00e0ff" valign=3D"top"> <div class=3D=
"e2ma-content-block"> <div class=3D"e2ma-p-div" style=3D"display: block;mar=
gin-bottom: 10px;font-size: 12px;font-weight: normal;line-height: 1.5;font-=
family: 'Open Sans', Helvetica, sans-serif;font-size: 14px;color: #333;font=
-family: 'Open Sans', Helvetica, sans-serif;font-size: 14px;color: #333;lin=
e-height: 30px; text-align: center"><span style=3D"line-height: 1.5"><span =
class=3D"e2ma-style" style=3D"background-color: transparent"><b>UNLIMITED A=
CCESS TO THE BEST MANAGEMENT RESOURCES</b></span></span></div>
<div class=3D"e2ma-p-div" style=3D"display: block;margin-bottom: 10px;font-=
size: 12px;font-weight: normal;line-height: 1.5;font-family: 'Open Sans', H=
elvetica, sans-serif;font-size: 14px;color: #333;font-family: 'Open Sans', =
Helvetica, sans-serif;font-size: 14px;color: #333;line-height: 25px; text-a=
lign:center"><span style=3D"line-height: 1.5"><span class=3D"e2ma-style" st=
yle=3D"background-color: transparent"><span class=3D"e2ma-style" style=3D"f=
ont-size: 14px">Subscribe today and get inventive strategies for leading in=
 a changing world from world-reknowned thought leaders and experts.</span><=
/span></span></div>
</div>
</td> </tr> </tbody></table> </td> </tr> </tbody></table>
<table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" class=3D"e2ma-block=
-outer" id=3D"block_yglmlsae" style=3D"font-family: Arial, Helvetica, sans-=
serif;font-size: 12px" width=3D"100%"> <tbody><tr> <td class=3D"e2ma-wrappe=
r e2ma-image-td" style=3D"padding-right: 0;padding-bottom: 0;padding-left: =
0;font-size: 12px;line-height: 1.5" valign=3D"top"> <table border=3D"0" cel=
lpadding=3D"0" cellspacing=3D"0" style=3D"font-family: Arial, Helvetica, sa=
ns-serif;font-size: 12px" width=3D"100%"> <tbody><tr> <td class=3D"e2ma-hol=
der" style=3D"padding: 40px 40px 20px 40px;background-color: transparent" v=
align=3D"top"> <div class=3D"e2ma-content-block"> <div class=3D"e2ma-p-div"=
 style=3D"display: block;margin-bottom: 10px;font-size: 12px;font-weight: n=
ormal;line-height: 1.5;font-family: 'Open Sans', Helvetica, sans-serif;font=
-size: 14px;color: #333;font-family: 'Open Sans', Helvetica, sans-serif;fon=
t-size: 14px;color: #333;text-transform: uppercase; font-family: &quot;Open=
 Sans&quot;, Helvetica, Arial, sans-serif; color: #1e89c2; letter-spacing: =
1px; text-align: center"><span style=3D"line-height: 1.5"><strong><span cla=
ss=3D"e2ma-style" style=3D"color: rgb(51, 51, 50)">Your Subscription Includ=
es:</span></strong></span></div>
</div>
</td> </tr> </tbody></table> </td> </tr> </tbody></table>
<table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" class=3D"e2ma-block=
-outer" id=3D"block_rijugjpa" style=3D"font-family: Arial, Helvetica, sans-=
serif;font-size: 12px" width=3D"100%"> <tbody><tr> <td class=3D"e2ma-wrappe=
r" style=3D"padding-right: 0;padding-bottom: 0;padding-left: 0" valign=3D"t=
op"> <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" style=3D"font-=
family: Arial, Helvetica, sans-serif;font-size: 12px" width=3D"100%"> <tbod=
y><tr> <td class=3D"e2ma-holder" style=3D"padding: 20px 40px 20px 40px;back=
ground-color: transparent" valign=3D"top"> <table align=3D"right" border=3D=
"0" cellpadding=3D"0" cellspacing=3D"0" style=3D"font-family: Arial, Helvet=
ica, sans-serif;font-size: 12px" width=3D"1%"> <tbody><tr> <td style=3D" pa=
dding: 10px 10px 10px 10px; " valign=3D"top" width=3D"1%"> <div align=3D"ce=
nter" style=3D"mso-table-lspace:0;mso-table-rspace:9"> <a href=3D"https://t=
.e2ma.net/click/bv2h2w/r3z1rkkb/brbmwpj" style=3D"font-weight: normal;font-=
weight: normal;color: #333;text-decoration: none;color: #333;text-decoratio=
n: none" target=3D"_blank"> <img alt=3D"Choose your subscription" border=3D=
"0" height=3D"220" src=3D"https://d31hzlhk6di2h5.cloudfront.net/20220407/ef=
/a4/9c/04/4e9524a57ea7e6b9ba037e45_560x440.png" style=3D"display: block" wi=
dth=3D"280"/> </a> </div>
</td> </tr> </tbody></table> <div class=3D"e2ma-combo-content" style=3D"fon=
t-size: 12px;line-height: 1.5"> <div class=3D"e2ma-p-div" style=3D"display:=
 block;margin-bottom: 10px;font-size: 12px;font-weight: normal;line-height:=
 1.5;font-family: 'Open Sans', Helvetica, sans-serif;font-size: 14px;color:=
 #333;font-family: 'Open Sans', Helvetica, sans-serif;font-size: 14px;color=
: #333;vertical-align: middle; text-align: left; font-size: 14px; mso-line-=
height: exactly; line-height: 120%; line-height: 19px; display: inline"><sp=
an style=3D"line-height: 1.5"><span style=3D"color: #ED1A36">=E2=80=A2</spa=
n> =C2=A0<span class=3D"e2ma-style" style=3D'font-family: "Open Sans", Helv=
etica, Arial, sans-serif'>Unlimited access to all new articles, reports, ca=
se studies, interviews, and videos</span></span></div>
<br/><br/> <div class=3D"e2ma-p-div" style=3D"display: block;margin-bottom:=
 10px;font-size: 12px;font-weight: normal;line-height: 1.5;font-family: 'Op=
en Sans', Helvetica, sans-serif;font-size: 14px;color: #333;font-family: 'O=
pen Sans', Helvetica, sans-serif;font-size: 14px;color: #333;vertical-align=
: middle; text-align: left; font-size: 14px; mso-line-height: exactly; line=
-height: 120%; line-height: 19px; display: inline"><span style=3D"line-heig=
ht: 1.5"><span style=3D"color: #ED1A36">=E2=80=A2</span> =C2=A0<span class=
=3D"e2ma-style" style=3D'font-family: "Open Sans", Helvetica, Arial, sans-s=
erif'>Unlimited access to over 30 years of back issues</span></span></div>
<br/><br/> <div class=3D"e2ma-p-div" style=3D"display: block;margin-bottom:=
 10px;font-size: 12px;font-weight: normal;line-height: 1.5;font-family: 'Op=
en Sans', Helvetica, sans-serif;font-size: 14px;color: #333;font-family: 'O=
pen Sans', Helvetica, sans-serif;font-size: 14px;color: #333;vertical-align=
: middle; text-align: left; font-size: 14px; mso-line-height: exactly; line=
-height: 120%; line-height: 19px; display: inline"><span style=3D"line-heig=
ht: 1.5"><span style=3D"color: #ED1A36">=E2=80=A2</span> =C2=A0<span class=
=3D"e2ma-style" style=3D'font-family: "Open Sans", Helvetica, Arial, sans-s=
erif'>New content every day=C2=A0=E2=80=94 including articles on the future=
 of work, artificial intelligence, digital transformation, strategy, leader=
ship, and more.</span></span></div>
<br/><br/> <div class=3D"e2ma-p-div" style=3D"display: block;margin-bottom:=
 10px;font-size: 12px;font-weight: normal;line-height: 1.5;font-family: 'Op=
en Sans', Helvetica, sans-serif;font-size: 14px;color: #333;font-family: 'O=
pen Sans', Helvetica, sans-serif;font-size: 14px;color: #333;vertical-align=
: middle; text-align: left; font-size: 14px; mso-line-height: exactly; line=
-height: 120%; line-height: 19px; display: inline"><span style=3D"line-heig=
ht: 1.5"><span style=3D"color: #ED1A36">=E2=80=A2</span>=C2=A0 A<span class=
=3D"e2ma-style" style=3D'font-family: "Open Sans", Helvetica, Arial, sans-s=
erif'>ccess to the iOS/Android app</span></span></div>
<br/><br/> <div class=3D"e2ma-p-div" style=3D"display: block;margin-bottom:=
 10px;font-size: 12px;font-weight: normal;line-height: 1.5;font-family: 'Op=
en Sans', Helvetica, sans-serif;font-size: 14px;color: #333;font-family: 'O=
pen Sans', Helvetica, sans-serif;font-size: 14px;color: #333;vertical-align=
: middle; text-align: left; font-size: 14px; mso-line-height: exactly; line=
-height: 120%; line-height: 19px; display: inline"><span style=3D"line-heig=
ht: 1.5"><span style=3D"color: #ED1A36">=E2=80=A2</span>=C2=A0 <span class=
=3D"e2ma-style" style=3D'font-family: "Open Sans", Helvetica, Arial, sans-s=
erif'>PDF downloads of all articles</span></span></div>
<br/><br/> <div class=3D"e2ma-p-div" style=3D"display: block;margin-bottom:=
 10px;font-size: 12px;font-weight: normal;line-height: 1.5;font-family: 'Op=
en Sans', Helvetica, sans-serif;font-size: 14px;color: #333;font-family: 'O=
pen Sans', Helvetica, sans-serif;font-size: 14px;color: #333;vertical-align=
: middle; text-align: left; font-size: 14px; mso-line-height: exactly; line=
-height: 120%; line-height: 19px; display: inline"><span style=3D"line-heig=
ht: 1.5"><span style=3D"color: #ED1A36">=E2=80=A2</span>=C2=A0 Weekly newsl=
etter with actionable insights<span class=3D"e2ma-style" style=3D'font-fami=
ly: "Open Sans", Helvetica, Arial, sans-serif'>=C2=A0</span></span></div>
<br/><br/> <div class=3D"e2ma-p-div" style=3D"display: block;margin-bottom:=
 10px;font-size: 12px;font-weight: normal;line-height: 1.5;font-family: 'Op=
en Sans', Helvetica, sans-serif;font-size: 14px;color: #333;font-family: 'O=
pen Sans', Helvetica, sans-serif;font-size: 14px;color: #333;vertical-align=
: middle; text-align: left; font-size: 14px; mso-line-height: exactly; line=
-height: 120%; line-height: 19px; display: inline"><span style=3D"line-heig=
ht: 1.5"><span style=3D"color: #ED1A36">=E2=80=A2</span> =C2=A0<span class=
=3D"e2ma-style" style=3D'font-family: "Open Sans", Helvetica, Arial, sans-s=
erif'><span style=3D"background-color: #ffe885"> Free copy of =E2=80=9C<str=
ong>Top 10 Lessons on Strategy</strong>=E2=80=9D =E2=80=94 78 pages of the =
most-read articles from the strategy archive</span> </span></span></div>
</div>
</td> </tr> </tbody></table> </td> </tr> </tbody></table>
<table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" class=3D"e2ma-block=
-outer e2ma-button" id=3D"block_wfuvxnck" style=3D"font-family: Arial, Helv=
etica, sans-serif;font-size: 12px" width=3D"100%"> <tbody><tr> <td class=3D=
"e2ma-wrapper" style=3D"padding-right: 0;padding-bottom: 0;padding-left: 0"=
 valign=3D"top"> <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" cl=
ass=3D"e2ma-holder" style=3D"font-family: Arial, Helvetica, sans-serif;font=
-size: 12px;padding: 20px 40px 40px 40px;background-color: transparent" wid=
th=3D"100%"> <tbody><tr> <td align=3D"center"> <table class=3D"c-collapsed-=
table" style=3D"font-family: Arial, Helvetica, sans-serif;font-size: 12px;b=
order-spacing: 0"> <tbody><tr> <td bgcolor=3D"#ed1a36" style=3D"-webkit-bor=
der-radius: 0px; -moz-border-radius: 0px; border-radius: 0px; box-sizing: b=
order-box; "> <a href=3D"https://t.e2ma.net/click/bv2h2w/r3z1rkkb/rjcmwpj" =
style=3D"font-weight: normal;font-weight: normal;color: #333;text-decoratio=
n: none;color: #333;text-decoration: none; padding: 16px 22px; font-size: 1=
8px; font-family: Arial, Helvetica, sans-serif; color: #ffffff; text-align:=
 center; text-decoration: none; border-radius: 0px; -webkit-border-radius: =
0px; -moz-border-radius: 0px; background-color: #ed1a36; font-style: normal=
; font-weight: bold; display: block; border: 1px solid #ed1a36; mso-line-he=
ight-rule: exactly; line-height:110%">Learn more =C2=BB</a> </td> </tr> </t=
body></table> </td> </tr> </tbody></table> </td> </tr> </tbody></table>
<table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" class=3D"e2ma-block=
-outer" id=3D"block_daykzuec" style=3D"font-family: Arial, Helvetica, sans-=
serif;font-size: 12px" width=3D"100%"> <tbody><tr> <td class=3D"e2ma-wrappe=
r e2ma-image-td" style=3D"padding-right: 0;padding-bottom: 0;padding-left: =
0;font-size: 12px;line-height: 1.5" valign=3D"top"> <table border=3D"0" cel=
lpadding=3D"0" cellspacing=3D"0" style=3D"font-family: Arial, Helvetica, sa=
ns-serif;font-size: 12px" width=3D"100%"> <tbody><tr> <td class=3D"e2ma-hol=
der" style=3D"padding: 40px;background-color: #292929" valign=3D"top"> <div=
 class=3D"e2ma-content-block"> <div class=3D"e2ma-p-div" style=3D"display: =
block;margin-bottom: 10px;font-size: 12px;font-weight: normal;line-height: =
1.5;font-family: 'Open Sans', Helvetica, sans-serif;font-size: 14px;color: =
#333;font-family: 'Open Sans', Helvetica, sans-serif;font-size: 14px;color:=
 #333;vertical-align: middle; text-align: center; mso-line-height: exactly;=
 line-height: 130%; line-height: 24px"><span style=3D"line-height: 1.5"><sp=
an class=3D"e2ma-style" style=3D'font-family: "Open Sans", Helvetica, Arial=
, sans-serif; color: #fff'><strong>=E2=80=9CI enjoy many publications, but =
@mitsmr is the release I look forward to the most! Whichever line of #busin=
ess, leadership, #technology, marketing, etc. you=E2=80=99re in, it=E2=80=
=99s worth far more than the subscription price.=E2=80=9D</strong><br/> <i>=
Michael Kanaan, U.S. Air Force Cochair for Artificial Intelligence</i></spa=
n></span></div>
</div>
</td> </tr> </tbody></table> </td> </tr> </tbody></table>
<table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" class=3D"e2ma-block=
-outer" id=3D"block_zewqpmke" style=3D"font-family: Arial, Helvetica, sans-=
serif;font-size: 12px" width=3D"100%"> <tbody><tr> <td class=3D"e2ma-wrappe=
r" style=3D"padding-right: 0;padding-bottom: 0;padding-left: 0" valign=3D"t=
op"> <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" style=3D"font-=
family: Arial, Helvetica, sans-serif;font-size: 12px" width=3D"100%"> <tbod=
y><tr> <td class=3D"e2ma-holder" style=3D"padding: 5px 40px 5px 40px;backgr=
ound-color: #e9e9e9" valign=3D"top"> <table border=3D"0" cellpadding=3D"0" =
cellspacing=3D"0" style=3D"font-family: Arial, Helvetica, sans-serif;font-s=
ize: 12px"> <tbody><tr><td valign=3D"top"><table border=3D"0" cellpadding=
=3D"0" cellspacing=3D"0" style=3D"font-family: Arial, Helvetica, sans-serif=
;font-size: 12px"><tbody><tr> <td class=3D"e2ma-image-td" style=3D"text-ali=
gn: center; padding: 10px 5px 10px 10px; " valign=3D"top"> <a href=3D"https=
://t.e2ma.net/click/bv2h2w/r3z1rkkb/7bdmwpj" style=3D"font-weight: normal;f=
ont-weight: normal;color: #333;text-decoration: none;color: #333;text-decor=
ation: none" target=3D"_blank"> <img alt=3D"Subscriptions" border=3D"0" hei=
ght=3D"20" src=3D"https://d31hzlhk6di2h5.cloudfront.net/20220407/35/db/d4/a=
8/621a5f3b962fcabb5bbf22e5_254x40.png" style=3D"display: block" width=3D"12=
7"/> </a> </td> <td class=3D"e2ma-image-td" style=3D"text-align: center; pa=
dding: 10px 5px 10px 5px; " valign=3D"top"> <a href=3D"https://t.e2ma.net/c=
lick/bv2h2w/r3z1rkkb/n4dmwpj" style=3D"font-weight: normal;font-weight: nor=
mal;color: #333;text-decoration: none;color: #333;text-decoration: none" ta=
rget=3D"_blank"> <img alt=3D"Collections" border=3D"0" height=3D"20" src=3D=
"https://d31hzlhk6di2h5.cloudfront.net/20220407/48/a2/dc/32/a59dcb3e48b8a45=
d453eace4_254x40.png" style=3D"display: block" width=3D"127"/> </a> </td> <=
td class=3D"e2ma-image-td" style=3D"text-align: center; padding: 10px 5px 1=
0px 5px; " valign=3D"top"> <a href=3D"https://t.e2ma.net/click/bv2h2w/r3z1r=
kkb/3wemwpj" style=3D"font-weight: normal;font-weight: normal;color: #333;t=
ext-decoration: none;color: #333;text-decoration: none" target=3D"_blank"> =
<img alt=3D"Back Issues" border=3D"0" height=3D"20" src=3D"https://d31hzlhk=
6di2h5.cloudfront.net/20220407/26/8b/38/22/5cb0935660eb422244344201_254x40.=
png" style=3D"display: block" width=3D"127"/> </a> </td> <td class=3D"e2ma-=
image-td" style=3D"text-align: center; padding: 10px 10px 10px 5px; " valig=
n=3D"top"> <a href=3D"https://t.e2ma.net/click/bv2h2w/r3z1rkkb/jpfmwpj" sty=
le=3D"font-weight: normal;font-weight: normal;color: #333;text-decoration: =
none;color: #333;text-decoration: none" target=3D"_blank"> <img alt=3D"Repo=
rts" border=3D"0" height=3D"20" src=3D"https://d31hzlhk6di2h5.cloudfront.ne=
t/20220407/47/bd/07/63/a0f3c6b7a89d655d8c957228_254x40.png" style=3D"displa=
y: block" width=3D"127"/> </a> </td> </tr></tbody></table></td></tr> </tbod=
y></table> </td> </tr> </tbody></table> </td> </tr> </tbody></table>
</td></tr></tbody></table></div>
<table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" class=3D"e2ma-row-r=
egion-content e2ma-section" style=3D"font-family: Arial, Helvetica, sans-se=
rif;font-size: 12px" width=3D"100%"><tbody><tr><td class=3D"e2ma-layout-col=
umn-content"></td></tr></tbody></table></td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td align=3D"center" bgcolor=3D"#F6F7F8" class=3D"e2ma-unsubscribe" style=
=3D"padding-bottom: 10px;padding-bottom: 10px;padding:10px 0px 50px 0px" va=
lign=3D"top">
<table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" class=3D"mobile-wid=
th" style=3D"font-family: Arial, Helvetica, sans-serif;font-size: 12px;widt=
h:640px">
<tbody>
<tr>
<td align=3D"left" valign=3D"top">
<table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" style=3D"font-famil=
y: Arial, Helvetica, sans-serif;font-size: 12px" width=3D"100%">
<tbody>
<tr>
<td align=3D"left" class=3D"stack" valign=3D"top">
<table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" style=3D"font-famil=
y: Arial, Helvetica, sans-serif;font-size: 12px" width=3D"100%">
<tbody>
<tr>
<td align=3D"center" style=3D"width:330px">
<table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" id=3D"template_foot=
er" style=3D"font-family: Arial, Helvetica, sans-serif;font-size: 12px;widt=
h:330px">
<tbody>
<tr>
<td align=3D"center" style=3D"width:286px">
<table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" style=3D"font-famil=
y: Arial, Helvetica, sans-serif;font-size: 12px;width:286px">
<tbody>
<tr>
<td align=3D"center" class=3D"footerlinks" style=3D"font-family:Helvetica, =
Arial, sans-serif; color:#9d9e9f; font-size:11px; text-align:center; paddin=
g-top:20px" valign=3D"top"> <div class=3D"e2ma-tag-outer">
<div class=3D"e2ma-p-div" style=3D"font-size: inherit"><a data-name=3D"Mana=
ge" data-type=3D"url" href=3D"https://t.e2ma.net/click/bv2h2w/r3z1rkkb/zhgm=
wpj" style=3D"font-weight: normal;font-weight: normal;color: #6b6c6e;text-d=
ecoration: none;color: #6b6c6e;text-decoration: none;font-weight: inherit">=
<strong>Manage</strong></a> your preferences</div>
</div>
</td>
<td align=3D"center" class=3D"center" style=3D"font-family:Helvetica, Arial=
, sans-serif; color:#9d9e9f; font-size:11px; text-align:center; padding-top=
:20px" valign=3D"top"><a href=3D'https://t.e2ma.net/optout/bv2h2w/r3z1rkkb?=
s=3DXrW3i9f7wULcJZLKglq1AxaLUbsOMjhroaDMKsmtJGk' style=3D"font-weight: norm=
al;font-weight: normal;color: #6b6c6e;text-decoration: none;color: #6b6c6e;=
text-decoration: none;color:#6b6c6e; text-decoration:none">| <strong>Opt ou=
t</strong></a> using <strong>TrueRemove=C2=AE</strong></td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td style=3D"width:305px">
<table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" style=3D"font-famil=
y: Arial, Helvetica, sans-serif;font-size: 12px;width:305px">
<tbody>
<tr>
<td align=3D"center" class=3D"footerlinks" style=3D"font-family:Helvetica, =
Arial, sans-serif; color:#9d9e9f; font-size:11px; text-align:center; paddin=
g:5px 0px 20px 0px" valign=3D"top"> <div class=3D"e2ma-tag-outer">
<div class=3D"e2ma-p-div" style=3D"font-size: inherit"><a data-name=3D"Sign=
 Up" data-type=3D"url" href=3D"https://t.e2ma.net/click/bv2h2w/r3z1rkkb/fah=
mwpj" style=3D"font-weight: normal;font-weight: normal;color: #6b6c6e;text-=
decoration: none;color: #6b6c6e;text-decoration: none;font-weight: inherit"=
><strong>Remove yourself</strong></a> from future special offers.</div>
</div>
</td>
<td align=3D"center" class=3D"center" style=3D"font-family:Helvetica, Arial=
, sans-serif; color:#9d9e9f; font-size:11px; text-align:center; padding:5px=
 0px 20px 0px" valign=3D"top">| View this email <a href=3D'https://t.e2ma.n=
et/message/bv2h2w/r3z1rkkb' style=3D"font-weight: normal;font-weight: norma=
l;color: #6b6c6e;text-decoration: none;color: #6b6c6e;text-decoration: none=
;color:#6b6c6e; text-decoration:none"><strong>online</strong></a>.</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td align=3D"center" class=3D"footer-text" style=3D"font-family:Helvetica, =
Arial, sans-serif; font-size:11px; line-height:1.5; text-align:center" vali=
gn=3D"top"><a href=3D"#" style=3D"font-weight: normal;font-weight: normal;c=
olor:#9d9e9f; text-decoration:none; pointer-events:none"> MIT Sloan Managem=
ent Review, One Main St., 9th floor, E90-9200 <br/>
                                                   Cambridge, MA | 02142 Un=
ited States=20
                                                   </a></td>
</tr>
<tr>
<td align=3D"center" class=3D"center" style=3D"font-family:Helvetica, Arial=
, sans-serif; color:#9d9e9f; font-size:11px; line-height:1.5; text-align:ce=
nter; padding-top:20px" valign=3D"top">This email was sent to <a href=3D"#"=
 style=3D"font-weight: normal;font-weight: normal;color:#9d9e9f; text-decor=
ation:none; pointer-events:none">jhomarcristianelias@gmail.com</a>. <br/>
<em>To continue receiving our emails, add us to your address book.</em>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td align=3D"left" style=3D"line-height:0px; font-size:0px" valign=3D"top">
<div style=3D"line-height:0px; font-size:0px"><img src=3D"https://t.e2ma.ne=
t/track/bv2h2w/r3z1rkkb" width=3D"1" height=3D"1"></div>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
</div>
</body></html>
""", subtype="html")


smtp.send_message(msg)