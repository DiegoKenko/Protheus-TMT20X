from escpos.printer import Usb
import usb.core
import usb.util
import usb.backend.libusb1
import sys
from datetime import datetime

 
#  sys.argv
# [1] Código do movimento de portaria
# [2] Nome do motorista
# [3] OC ou SCM
# [4] Código da OC ou da SCM
# [5] Nome do usuário do protheus
# [6] tipo da refeição [1]café [2]almoço [3]janta

agora = datetime.now().strftime("%d/%m/%Y  |  %H:%M")
   
p = Usb(0x04B8, 0x0E27, 0, 0x81, 0x02) # Específico para impressora Epson TM-T20X
p.set(double_width=True,double_height=True)
p.control('HT')
p.text("    TICKET REFEICAO")
p.set(double_width=True,double_height=False)
p.ln()
p.ln()
p.text('       '  + sys.argv[1] )
p.ln()
p.ln()
p.text('   '  + sys.argv[2].replace('_',' '))
p.ln()
p.ln()
p.text('     '  + sys.argv[3] + ' ' + sys.argv[4])
p.ln()
p.ln()
if sys.argv[6] == '1':
     p.text('         '  +"Cafe")
elif sys.argv[6] == '2':
     p.text('          '  +"Almoco")
elif sys.argv[6] == '3':
     p.text('         '  +"Janta")
p.ln()
p.ln()
p.text('   '  +sys.argv[5].replace('_',' '))
p.ln()
p.text('  '  +agora)
p.ln()
p.ln()
p.text("_______________________")
p.ln()
p.cut(mode='FULL')

