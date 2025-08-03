CXX = clang++
CXXFLAGS = -std=c++17 -Wall -Wextra

TARGET = query_db
SRCS = query_db.cpp

$(TARGET): $(SRCS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SRCS)

.PHONY: clean
clean:
	rm -f $(TARGET)
