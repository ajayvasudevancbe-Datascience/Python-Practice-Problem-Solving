""" Question 9: get_averages_from_csv """
"""
Input: two strings, one representing a csv and one representing a header
Output: average of csv entries under header
        None if header does not appear in csv or if values in column are not integers
"""
def row_to_list(row):
    L = row.split(",")
    for i in range(len(L)):   
       if (L[i].isdigit()):
            L[i] = int(L[i])
    return L


def csv_to_row(s):
  s = s.strip()
  University = list()
  for row in s.splitlines():
    new_row = row_to_list(row)   
    University.append(new_row)
  return University


def get_averages_from_csv(csv_str, header):
  new_list = csv_to_row(csv_str)
  head = new_list[0]
  count = 0
  Averages = 0
  result = 0
  if(header==head[1]):
       for i in range(1,len(new_list)):
           result+=new_list[i][1]
           count+=1
       Averages=result/count 
       return Averages
  if(header==head[2]):  
      for j in range(1,len(new_list)):
          result+=new_list[j][2]
          count+=1
      Averages=result/count
      return Averages 


""" Test 9 """
def test_get_averages_from_csv():
    print("Testing get_averages_from_csv...", end='')
    csv = """University,Number of Students,Tuition
Carnegie Mellon University,13961,76760
Stanford University,16914,78218
Harvard University,22947,75891
University of California Berkeley,45057,41528"""
    assert(get_averages_from_csv(csv, "Number of Students") == 24719.75)
    assert(get_averages_from_csv(csv, "University") == None)
    assert(get_averages_from_csv(csv, "Tuition") == 68099.25)
    assert(get_averages_from_csv(csv, "Undergrad Population") == None)
    print("... done!")

if __name__ == '__main__':
    test_get_averages_from_csv()