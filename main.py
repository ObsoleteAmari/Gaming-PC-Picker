redirect = '<meta http-equiv = "refresh" content = "0; url = {url}" />'
def product(budget):
    if budget<51:
        return("Unfortunately,there are no good Gaming PCs available for that price.\n"+redirect.format(url="https://www.amazon.co.uk/Samsung-MZ-76E500B-EU-Solid-State/dp/B078WQT6S6/"))
    elif budget<400:
        return("Unfortunately, there are no good gaming PCs available for that price.\n"+redirect.format(url="https://www.amazon.co.uk/Corsair-Vengeance-Enthusiast-Illuminated-Memory/dp/B07D1XCKWW/",text="Here is a memory kit instead?"))
    elif budget>399 and budget<450:
        return(redirect.format(url="https://www.amazon.co.uk/Fast-Gaming-Computer-Bundle-Generation/dp/B08GD1MS8C/"))
    elif budget>449 and budget<500:
        return(redirect.format(url="https://www.amazon.co.uk/Fierce-Gaming-PC-Bundle-Compatible/dp/B071KXJ65V/"))
    elif budget>499 and budget<550:
        return(redirect.format(url="https://www.amazon.co.uk/Fierce-MANTA-Gaming-PC-Bundle/dp/B07DXZR6LR/"))
    elif budget>599 and budget<700:
        return(redirect.format(url="https://www.amazon.co.uk/Fierce-MANTA-Gaming-PC-Bundle/dp/B07DY13H3G/"))
    else:
        return(redirect.format(url="https://www.amazon.co.uk/Precision-Computer-Dual-Core-Processor-Graphics/dp/B016C743XY/"))
budget=int(input('Hello! This is a tool to help you choose a gaming PC.\nI am not sponsored by anyone; this was just made for fun. \n Please do not type the £ sign, just the number. \nType your budget. Max is currently £700 because anything above that likely is not worth it.\nStill a work in progress!\n'))
with open("index.html","w+") as html:
  html.write(product(budget))
# I'm working on linking the output to a html document so it looks better but it isn't working yet.