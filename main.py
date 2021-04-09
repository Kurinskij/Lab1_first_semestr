from logic import Game_of_life
class Main(Game_of_life):
    obj=Game_of_life()
    obj.transformation_data(obj.read_from_file("datafile"))
    #for i in obj.data_table:
      #  print(i)
    obj.generation_after_step(obj.data_table,obj.generation)
    obj.write_in_file("datafile",obj.retransformation_data(obj.data_table))

exam=Main()
