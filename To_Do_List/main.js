// Get references to the HTML elements
const categoryInput = document.getElementById('category');
const taskInput = document.getElementById('task');
const tasksList = document.getElementById('tasks-list');

// Create an object to store tasks by category
const tasksByCategory = {};

// Function to add a task to a category
function addTask() {
    // Get the values from the input fields
    const category = categoryInput.value;
    const task = taskInput.value;

    // Check if both category and task are filled
    if (category === '' || task === '') {
        alert('Please enter both a category and a task.');
        return; // Stop here if inputs are empty
    }

    // If the category doesn't exist yet, create an empty array for it
    if (!tasksByCategory[category]) {
        tasksByCategory[category] = [];
    }

    // Add the task to the array for the category
    tasksByCategory[category].push(task);

    // Clear the input fields
    categoryInput.value = '';
    taskInput.value = '';

    // Show the updated task list
    listTasks();
}

// Function to show all tasks on the page
function listTasks() {
    // Clear the current list of tasks
    tasksList.innerHTML = '';

    // Loop through each category in tasksByCategory
    for (let category in tasksByCategory) {
        // Create a div for the category and add its name
        const categoryDiv = document.createElement('div');
        categoryDiv.className = 'category';

        const categoryTitle = document.createElement('h3');
        categoryTitle.textContent = category;
        categoryDiv.appendChild(categoryTitle);

        // Loop through the tasks in this category
        tasksByCategory[category].forEach(function (task, index) {
            // Create a div for each task and a remove button
            const taskDiv = document.createElement('div');
            taskDiv.className = 'task';

            const taskSpan = document.createElement('span');
            taskSpan.textContent = task;
            taskDiv.appendChild(taskSpan);

            // Create a remove button for each task
            const removeButton = document.createElement('button');
            removeButton.textContent = 'Remove';
            removeButton.onclick = function () {
                removeTask(category, index);
            };
            taskDiv.appendChild(removeButton);

            // Add the task div to the category div
            categoryDiv.appendChild(taskDiv);
        });

        // Add the category div to the main task list
        tasksList.appendChild(categoryDiv);
    }
}

// Function to remove a task
function removeTask(category, taskIndex) {
    // Remove the task from the category's array
    tasksByCategory[category].splice(taskIndex, 1);

    // If the category has no tasks left, remove the category
    if (tasksByCategory[category].length === 0) {
        delete tasksByCategory[category];
    }

    // Update the task list
    listTasks();
}
