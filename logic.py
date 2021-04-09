"""str_data="6" \
         "5 6" \
         "***X**" \
         "*X****" \
         "***X**" \
         "*****X" \
         "******"""
class Game_of_life():

    generation=0
    string=0
    column=0
    data_table=[]

    def read_from_file(self,filename):
        file = open(filename)
        string_table=file.read().splitlines()
        file.close()
        return string_table

    def transformation_data(self,table_str):
        self.generation = int(table_str.pop(0))
        self.string,self.column = map(int,table_str.pop(0).split(" "))
        for line in table_str:
            list_line=[]
            for elements in line:
                if elements=="*":
                    list_line.append(False)
                else:list_line.append(True)
            self.data_table.append(list_line)

    def next_points_state(self,coordinateY,coordinateX,plant):
        next_state=False
        coordinate_neignbour=[]
        for y in range(coordinateY-1,coordinateY+2):
            for x in range(coordinateX - 1, coordinateX + 2):
                if (x,y)!=(coordinateX,coordinateY):
                    coordinate_neignbour.append([y,x])
        for pair in  coordinate_neignbour:
            if pair[0]<0:pair[0]=len(plant)-1
            if pair[1] < 0: pair[1] = len(plant[0]) - 1
            if pair[0] == len(plant): pair[0] = 0
            if pair[1] == len(plant[0]): pair[1] = 0

        numbers_neighbour=len([i for i in coordinate_neignbour if plant[i[0]][i[1]]==True])
        if plant[coordinateY][coordinateX]==True:
            if numbers_neighbour>=2 and numbers_neighbour<=3:
                next_state=True
        else:
            if numbers_neighbour == 3:
                next_state = True

        return next_state

    def next_field_state(self,plant):
        next_state=[[self.next_points_state(y,x,plant) for x in range(len(plant[0]))]for y in range(len(plant)) ]
        return next_state

    def generation_after_step(self,plant,step):
        while step>0:
            plant=self.next_field_state(plant)
            step-=1
        return plant

    def retransformation_data(self,table):
        string_table=[]
        for i in table:
            line = ''
            for j in i:
                if j==False:
                    line+='*'
                else: line+='x'
            string_table.append(line)
        return string_table

    def write_in_file(self,filename,data):
        file = open(filename, 'w')
        for line in data:
            file.write(line+'\n')
        file.close()


#obj =Game_of_life()
#obj.read_from_file("datafile")
#obj.transformation_data(a)
#for i in(obj.data_table):
#    print(i)
#for i in obj.data_table:
 #   print(i)
#obj.next_points_state(1,3)
#obj.generation_after_step()
#for i in obj.data_table:
#    print(i)