char m[20] = { 'D','x','x','X','T','B','Y','i','W','m','H','P','f','e','K','_','_','_','r','m'};
  char* arr = new char[20];
  for (int i = 0; i < 20; i++) {
      arr[i] = m[i];
  }

  std::cout << is_identifier(arr);