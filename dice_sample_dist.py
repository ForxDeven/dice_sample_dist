'''
A sample distribution creator for die throws
Author: Ali Altuntas, METU Statistics, 2023
'''
import random as rand

def mean(lst): #mean function for a list input
    return sum(lst) / len(lst)

def std_dev(test_list): #standard deviation function for a list input, returns standard dev. you can also make it return variance
    avg0 = mean(test_list)
    variance = sum([((x - avg0) ** 2) for x in test_list]) / len(test_list)
    return variance ** 0.5

def sample_mean_saver(lst): #a function for user to save sample means to a .txt file
    title = input("File title: ")  #user inputs a file title
    filetitle = title + ".txt" #creates the full file title with .txt
    file = open(filetitle,"w+") #opens the file
    file.write(str(lst)) #writes the list to the file
    file.close() #closes the file

#info
print("***************************\nThis program shows a sample distrubiton of sample means for dice throws.\nYou need to enter how many samples you want first and then enter sample size you want.")
print("The program will provide you population mean, population standard deviation, a sample distrubiton table, mean of sample means, standard deviation of sample means")
print("\n***************************")

sample_num = int(input("Enter amount of samples :"))    #amount of samples  | user enters
n = int(input("Enter sample size        :"))            #sample size        | user enters
print("\n\n\n")

population = [1,2,3,4,5,6] #population of a die
sample_means = []   #an empty list to save sample means later
sample = [] #an empty list to save each element in a sample
for i in range(sample_num):
    for j in range(n): #creates a sample
        num = rand.randint(1,6) #throws a die (crates a random number from 1 to 6)
        sample.append(num) #adds the result into sample

    avg = mean(sample) #calculates sample mean

    sample_means.append(avg) #adds sample mean to the sample means list
    sample = [] #reset the sample

#Possible sample mean results 
avg100 = "1.00  |"
avg125 = "1.25  |"
avg150 = "1.50  |"
avg175 = "1.75  |"
avg200 = "2.00  |"
avg225 = "2.25  |"
avg250 = "2.50  |"
avg275 = "2.75  |"
avg300 = "3.00  |"
avg325 = "3.25  |"
avg350 = "3.50  |"
avg375 = "3.75  |"
avg400 = "4.00  |"
avg425 = "4.25  |"
avg450 = "4.50  |"
avg475 = "4.75  |"
avg500 = "5.00  |"
avg525 = "5.25  |"
avg550 = "5.50  |"
avg575 = "5.75  |"
avg600 = "6.00  |"

#If you want to save the sample means, delete the hash symbol
#sample_mean_saver(sample_means)

#the code below creates the output
for avg_s in sample_means:
    
    if avg_s == 1.0:
        avg100 = avg100 + "X"
    elif avg_s == 1.25:
        avg125 = avg125 + "X"
    elif avg_s == 1.5:
        avg150 = avg150 + "X"
    elif avg_s == 1.75:
        avg175 = avg175 + "X"
    elif avg_s == 2.0:
        avg200 = avg200 + "X"
    elif avg_s == 2.25:
        avg225 = avg225 + "X"
    elif avg_s == 2.5:
        avg250 = avg250 + "X"
    elif avg_s == 2.75:
        avg275 = avg275 + "X"
    elif avg_s == 3.0:
        avg300 += "X"
    elif avg_s == 3.25:
        avg325 += "X"
    elif avg_s == 3.5:
        avg350 += "X"
    elif avg_s == 3.75:
        avg375 += "X"
    elif avg_s == 4.0:
        avg400 += "X"
    elif avg_s == 4.25:
        avg425 += "X"
    elif avg_s == 4.5:
        avg450 += "X"
    elif avg_s == 4.75:
        avg475 += "X"
    elif avg_s == 5.0:
        avg500 += "X"
    elif avg_s == 5.25:
        avg525 += "X"
    elif avg_s == 5.5:
        avg550 += "X"
    elif avg_s == 5.75:
        avg575 += "X"
    elif avg_s == 6.0:
        avg600 += "X"
print("Population Mean  :" + str(mean(population)) + "\nPopulation S.dev :" + str(std_dev(population)) + "\n" + avg100 + "\n" +avg125 + "\n" +avg150 + "\n" +avg175 + "\n" +avg200 + "\n" +avg225 + "\n" +avg250 + "\n" +avg275 + "\n" +avg300 + "\n" +avg325 + "\n" +avg350 + "\n" +avg375 + "\n" +avg400 + "\n" +avg425 + "\n" +avg450 + "\n" +avg475 + "\n" +avg500 + "\n" +avg525 + "\n" +avg550 + "\n" +avg575 + "\n" +avg600 + "\n" + "Mean  :" +str(mean(sample_means)) + "\n" + "S.dev :" +str(std_dev(sample_means)))