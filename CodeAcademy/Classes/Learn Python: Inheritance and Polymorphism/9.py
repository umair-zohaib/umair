class SortedList(list):
  def append(self, value):
    super().append(value)
    self.sort()