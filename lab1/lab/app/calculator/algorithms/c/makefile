.PHONY : clean release debug
CC = gcc
CFLAGS = -std=c99 -Wall -Wextra -fPIC

INC_DIR = ./inc
OBJ_DIR = ./out
SRC_DIR = ./src

MyDistances.so: $(OBJ_DIR)/Distances.o
	$(CC) -shared $(OBJ_DIR)/Distances.o -o $@

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) -I$(INC_DIR) -c $< -o $@

$(OBJ_DIR)/%.d: $(SRC_DIR)/%.c
	@mkdir -p $(@D)
	$(CC) -MM -I$(INC_DIR) -MT '$(@:.d=.o)' $< > $@

include $(OBJECTS:.o=.d)
	
clean:
	rm -f -r $(OBJ_DIR) *.exe *.so __pycache__ .pytest_cache
