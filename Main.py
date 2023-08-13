from difflib import SequenceMatcher

from final import mark  

def similar(a,b):
    return SequenceMatcher(None,a,b).ratio()


from gui1 import tanswer,sanswer,keyword1


a=float(similar(tanswer,sanswer))
print(a)

if keyword1 in sanswer:

 if a>=0.90:

   marks=5

 elif a>=0.80:

    marks=4

 elif a>=0.70:

    marks=3

 elif a>=0.60:
    
   marks=2

 elif a>=0.50:
     
     marks=1

 else:
  marks=0

else:
  if a>=0.90:

          marks=4

  elif a>=0.80:

    marks=3

  elif a>=0.70:
  
    marks=2

  elif a>=0.60:

     marks=1

  else: 

    marks=0

fmark=marks