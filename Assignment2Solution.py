import psutil


if __name__ == '__main__':
    print('Monitoring CPU usage ...')
    process = psutil.Process()

    per = int(process.cpu_percent(interval=0.1)) * 100
    print(per)

    while(True):
        if per in range (0, 80):
            print ("Alert!! Normal working")
        elif per in range(85 , 90):
            print ("Alert!! CPU usage exceeds threshold 85%")
        else:
             print ("Alert!! CPU usage exceeds threshold 90%")
        
        print(per)


