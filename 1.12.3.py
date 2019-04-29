def main():
    celsius=0
    fareinheit=50
    while fareinheit<=150:
        celsius=5/9*(fareinheit-32)
        print("%.1f°C = %d°F"%(celsius,fareinheit))
        fareinheit+=1
    return 0

main()