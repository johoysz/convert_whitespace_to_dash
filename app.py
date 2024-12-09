def spaceToDash(txt):
    txt_dash = txt.replace(' ','-');
    return txt_dash

if __name__ == "__main__":
    while True:
        txt = input("\nEnter your sentence (or press ENTER to exit): ")
        if txt == "":
            print("\n//////////goodbyeeee..................///////")
            break
        print(spaceToDash(txt))
