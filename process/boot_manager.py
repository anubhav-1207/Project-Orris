from tqdm import tqdm
import time

print("\nPlease Wait....")
time.sleep(1)

def boot_manager():
    print('')
    for i in tqdm(range(100)):
        time.sleep(0.1)

    print("\nInitialising Files....")
    time.sleep(1)
    print("Checking Memory Status....")
    time.sleep(2)
    print("Finished.")
    
    while True:
        line = input(">>> ~$ ")



