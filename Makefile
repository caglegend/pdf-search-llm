# Python and C++ Settings
PYTHON = py -3
CXX = g++
CXXFLAGS = -O2 -std=c++17

# Files 
SEARCH = cpp/search.cpp
BINARY = search
PDF = tests/MachineLearningTomMitchell.pdf
TXT = tests/sample.txt
KEYWORD = "machine learning"

all: run

# C++ binary
$(BINARY): $(SEARCH)
	$(CXX) $(CXXFLAGS) $(SEARCH) -o $(BINARY)

# PDF to TXT
$(TXT): $(PDF)
	$(PYTHON) python/pdf_to_text.py $(PDF) $(TXT)

# Run
run: $(BINARY) $(TXT)
	./$(BINARY) $(TXT) $(KEYWORD)

# Clean
clean:
	rm -f $(BINARY) $(TXT)
