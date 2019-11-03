#For the initial amount of streams and their flow
numberofstreams = int(input())
streams = []
for i in range(numberofstreams):
    streams.append(int(input()))

#For all the splits and joints between the rivers
splitsandjoins = []
doneasking = False
while not doneasking:

    splitorjoin = int(input())
    if splitorjoin == 99: #A split
        streamnumber = int(input())
        percentagetotheleft = int(input())/100
        stream = streamnumber-1 #gets the index of the stream that was split

        rightfork = round(streams[stream]-(streams[stream]*percentagetotheleft)) #creates the new value (of flow) for the old stream
        leftfork = round(streams[stream]*percentagetotheleft)
        streams.remove(streams[stream])
        streams.insert(stream, rightfork)
        streams.insert(stream, leftfork)  # creates the new stream
        #try deleting all values that have been influenced and replacing them with new ones

    elif splitorjoin == 88: #A join
        streamnumber = int(input()) #The 'chosen' stream
        stream = streamnumber-1 #finds the index of the stream that is to be joind with the stream to its right

        newstream = streams[stream]+streams[stream+1] #adds the flow values to the chosen stream
        #I thin kthis is wrong if the given index is 0
        streams.remove(streams[stream+1])
        streams.remove(streams[stream])
        streams.insert(stream, newstream)

    elif splitorjoin == 77:
        doneasking = True

#Finalizes and readies the data to be outputted
#streams = [round(x) for x in streams]
final = ""
for i in streams:
    print(i, end=" ")