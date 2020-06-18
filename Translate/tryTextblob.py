from textblob import TextBlob

text = """
what I am envisioning is that someday we can stop doing some hurt each other"
"""
print(f"\nTranslated to Chinese: {TextBlob(text).translate(to='zh')}\n")
print(f"Translated to French: {TextBlob(text).translate(to='fr')}\n")
print(f"Translated to Japanese: {TextBlob(text).translate(to='ja')}")



