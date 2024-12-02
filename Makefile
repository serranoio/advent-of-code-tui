DAYS := $(shell seq 1 25)
DIRS := $(addprefix day-,$(DAYS))

FILES := $(foreach dir,$(DIRS),$(wildcard $(dir)/part-*.py))

.PHONY: all
all: $(FILES)

day-1/part-%:
	@echo "Day 1: Historian Hysteria"
	@chmod +x $@.py
	@./get-data.py --day 1 | python3 $@.py || true

.PHONY: help
help:
	@echo "Usage:"
	@echo "  make all               - Run all puzzles from all days"
	@echo "  make day-n/part-x      - Run a specific puzzle (replace n with the day and x with the part name)"
	@echo "  make clean             - Clean up generated files (if applicable)"
	@echo "  make help              - Show this help message"

.PHONY: clean
clean:
	@echo "Cleaning up"
	@rm -f *.out *.log 
