def calculate_minimum_runtime(maxBattery, startBattery, taskList, chargingSpeed):

    currentLevel = startBattery
    totalRuntime = 0.0

    for task in taskList:

        taskDuration = task[0]
        batteryUsagePerSec = task[1]

        # Total battery needed for this task
        requiredBattery = taskDuration * batteryUsagePerSec

        # Impossible case:
        # Even a full battery cannot support this task
        if requiredBattery > maxBattery:
            return -1.0

        # If battery is insufficient, calculate charging time
        if currentLevel < requiredBattery:

            missingBattery = requiredBattery - currentLevel

            # Cannot recharge
            if chargingSpeed <= 0:
                return -1.0

            waitingTime = missingBattery / chargingSpeed

            totalRuntime += waitingTime
            currentLevel += missingBattery

            # Extra safety
            if currentLevel > maxBattery:
                currentLevel = maxBattery

        # Execute task
        currentLevel -= requiredBattery

        # Add task execution duration
        totalRuntime += taskDuration

    return round(totalRuntime, 1)


# Sample test case
batteryCapacity = 100
initialBattery = 50

tasks = [
    [10, 5],
    [5, 8],
    [20, 2]
]

chargeRate = 4

answer = calculate_minimum_runtime(
    batteryCapacity,
    initialBattery,
    tasks,
    chargeRate
)

print("Minimum Total Runtime =", answer)