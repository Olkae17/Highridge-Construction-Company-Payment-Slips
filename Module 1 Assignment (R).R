set.seed(123)

# Generate worker data
workers <- data.frame(
  id = 1:500,
  name = paste("Worker", 1:500, sep="_"),
  salary = sample(4000:40000, 500, replace = TRUE),
  gender = sample(c("Male", "Female"), 500, replace = TRUE)
)

# Assign employee levels
workers$level <- ifelse(workers$salary > 10000 & workers$salary < 20000, "A1",
                        ifelse(workers$salary > 7500 & workers$salary < 30000 & workers$gender == "Female", "A5-F", "B2"))

# Print payment slips
print(workers)
