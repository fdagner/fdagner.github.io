document.addEventListener('DOMContentLoaded', function () {
    const sliderLabelText = "Slider";
    const slidersContainer = document.querySelector('.sliders-container');
    const addSliderBtn = document.getElementById('addSliderBtn');
    const fileInput = document.getElementById('fileInput');
    const saveButton = document.getElementById('saveButton');
    const clearButton = document.getElementById('clearBtn');
    const chartContainer = document.querySelector('#spiderChart');
    const jsonFileSelect = document.getElementById('jsonFileSelect');
    const loadJsonButton = document.getElementById('loadJsonButton');
    let slidersData = [];
    let chart = null;

    // Function to create a slider
    function createSlider(name = '', value, leftText = '', rightText = '') {
        const sliderGroup = document.createElement('div');
        sliderGroup.classList.add('slider-group');

        const lrContainer = document.createElement('div');
        lrContainer.classList.add('slider-lr');

        const leftInput = createInputField('', leftText, 45, function (sliderGroup, value) {
            updateSliderValue(sliderGroup, value);
        }, sliderGroup);
        const rightInput = createInputField('', rightText, 45, function (sliderGroup, value) {
            updateSliderValue(sliderGroup, value);
        }, sliderGroup);
        leftInput.classList.add('slider-left');
        rightInput.classList.add('slider-right');

        const input = document.createElement('input');
        input.type = 'range';
        input.classList.add('slider');
        input.min = 0;
        input.max = 10;
        input.step = 0.5;
        input.value = value;

        const valueDisplay = document.createElement('span');
        valueDisplay.classList.add('slider-value');
        valueDisplay.textContent = value;

        const nameInput = createInputField('', name, 60, function (sliderGroup, value) {
            updateSliderName(sliderGroup, value);
        }, sliderGroup);
        nameInput.classList.add('slider-name');
        nameInput.placeholder = `${sliderLabelText} ${slidersContainer.children.length + 1}`;

        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = 'x';
        deleteBtn.classList.add('delete-slider-btn');
        deleteBtn.addEventListener('click', function () {
            deleteSlider(sliderGroup);
            updateRadar();
        });

        input.addEventListener('input', function () {
            valueDisplay.textContent = this.value;
            updateSliderValue(sliderGroup, this.value);
            updateRadar();
        });

        // Create a div to hold nameInput and deleteBtn
        const nameDeleteContainer = document.createElement('div');
        nameDeleteContainer.classList.add('name-delete-container');
        nameDeleteContainer.appendChild(nameInput);
        nameDeleteContainer.appendChild(deleteBtn);

        lrContainer.appendChild(leftInput);
        lrContainer.appendChild(input);
        lrContainer.appendChild(rightInput);

        sliderGroup.appendChild(nameDeleteContainer);  // Append the new div to sliderGroup
        sliderGroup.appendChild(valueDisplay);
        sliderGroup.appendChild(lrContainer);
        slidersContainer.appendChild(sliderGroup);

        slidersData.push({ name, value: parseFloat(value), leftText, rightText });
        updateRadar();
    }

    let fieldCounter = 0; // Initialize a global counter for unique IDs

    // Function to create input fields for slider's name, left, and right labels
    function createInputField(placeholder, value, maxLength, updateValueCallback, sliderGroup) {
        const input = document.createElement('input');
        input.type = 'text';
        input.placeholder = placeholder;
        input.value = value;
        input.maxLength = 90;

        const uniqueId = `${placeholder.replace(/\s+/g, '_').toLowerCase()}_input_${fieldCounter++}`;
        input.id = uniqueId;
        input.name = uniqueId;

        // Event listener for the input field
        input.addEventListener('input', function () {
            if (this.value.length > maxLength) {
                alert(`Der Text darf nicht länger als ${maxLength} Zeichen sein.`);
                this.value = this.value.slice(0, maxLength);
            }

            // Check if it's the name field
            const isNameField = input.classList.contains('slider-name');

            // If it is the name field, update the chart
            if (isNameField) {
                updateValueCallback(sliderGroup, this.value);
                updateRadar();
            } else {
                return;
            }
        });
        return input;
    }

    // Function to delete a slider
    function deleteSlider(sliderGroup) {
        if (slidersContainer.children.length <= 3) {
            alert("Es müssen mindestens drei Kriterien vorhanden sein");
            return;
        }
        const sliderIndex = Array.from(slidersContainer.children).indexOf(sliderGroup);
        if (sliderIndex >= 0 && sliderIndex < slidersData.length) {
            slidersData.splice(sliderIndex, 1);
        }
        sliderGroup.remove();
        updateRadar();
    }

    // Function to update the name of a slider
    function updateSliderName(sliderGroup, newName) {
        const sliderIndex = Array.from(slidersContainer.children).indexOf(sliderGroup);
        if (sliderIndex >= 0 && sliderIndex < slidersData.length) {
            slidersData[sliderIndex].name = newName;
            updateRadar();
        }
    }

    // Function to update the value of a slider
    function updateSliderValue(sliderGroup, newValue) {
        const sliderIndex = Array.from(slidersContainer.children).indexOf(sliderGroup);
        if (sliderIndex >= 0 && sliderIndex < slidersData.length) {
            slidersData[sliderIndex].value = parseFloat(newValue);
        }
    }

    // Function to update the radar chart
    function updateRadar() {
        let sliderNames = slidersData.map(slider => slider.name);
        const initialData = slidersData.map(slider => slider.value);

        if (chart) {
            chart.updateOptions({
                xaxis: { categories: sliderNames },
                series: [{ data: initialData }]
            });
        } else {
            const chartOptions = {
                series: [{ name: 'Rating', data: initialData }],
                chart: {
                    width: "100%", type: 'radar'
                },
                xaxis: {
                    categories: sliderNames,
                    labels: { show: true, style: { fontSize: '14px', colors: Array(33).fill('#000') } }
                },
                yaxis: { max: 10, tickAmount: 5 },
                plotOptions: {
                    radar: {
                        polygons: { strokeColors: '#e9e9e9', fill: { colors: ['#e9e9e9', '#fff'] } }
                    }
                },
                stroke: { width: 2 },
                markers: { size: 6, colors: ['#ffffff'], strokeColors: '#33b2df', strokeWidth: 1 },
                fill: { colors: ['#33b2df'], opacity: 0.2 },
                title: { text: '', align: 'center' },
                responsive: [{
                    breakpoint: 768,
                    stroke: { width: 1 },
                    options: {
                        markers: { size: 3, colors: ['#ffffff'], strokeColors: '#33b2df', strokeWidth: 2 },
                        xaxis: {
                            labels: {
                                style: {
                                    fontSize: '11px',
                                },
                                plotOptions: {
                                    radar: {
                                        size: 70,
                                       }
                                },
                            }
                        },

                    }
                }]
            };
            chart = new ApexCharts(chartContainer, chartOptions);
            chart.render();
        }
    }

    // Function to initialize default sliders
    function initializeSliders() {
        slidersData = [];
        const defaultSliders = [
            { name: '', value: 5, leftText: '', rightText: '' },
            { name: '', value: 5, leftText: '', rightText: '' },
            { name: '', value: 5, leftText: '', rightText: '' }
        ];

        defaultSliders.forEach(slider => {
            createSlider(slider.name, slider.value, slider.leftText, slider.rightText);
        });
    }

    // Event: Add new slider
    addSliderBtn.addEventListener('click', function () {
        const currentSliderCount = slidersContainer.children.length;
        if (currentSliderCount >= 15) {
            alert("Sie können nur bis zu 15 Regler hinzufügen.");
        } else {
            createSlider("", 5);
        }
    });

    // Event: Button to load JSON data
    loadJsonButton.addEventListener('click', function () {
        const selectedFile = jsonFileSelect.value;
        if (selectedFile) {
            loadJsonData(selectedFile);
        }
    });

    // Function to load JSON data from a file
    function loadJsonData(filename) {
        fetch(filename)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                slidersContainer.innerHTML = '';
                slidersData = [];
                if (data.sliders && Array.isArray(data.sliders)) {
                    data.sliders.forEach(slider => {
                        createSlider(slider.name, slider.value, slider.leftText, slider.rightText);
                    });
                } else {
                    alert('Invalid data structure.');
                }
            })
            .catch(error => {
                console.error('Error loading file:', error);
                alert('Error loading file.');
            });
    }

    // Event: Upload JSON file
    fileInput.addEventListener('change', function (event) {
        const file = event.target.files[0];
        if (file && file.type === 'application/json') {
            const reader = new FileReader();
            reader.onload = function (e) {
                try {
                    const data = JSON.parse(e.target.result);
                    if (!Array.isArray(data.sliders) || data.sliders.length < 3) {
                        alert('Invalid data.');
                        return;
                    }
                    slidersContainer.innerHTML = '';
                    slidersData = [];
                    data.sliders.forEach(slider => {
                        createSlider(slider.name, slider.value, slider.leftText, slider.rightText);
                    });
                } catch {
                    alert('Error loading file.');
                }
            };
            reader.readAsText(file);
        } else {
            alert('Invalid file.');
        }
        fileInput.value = '';
    });

    // Event: Save data
    saveButton.addEventListener('click', function () {
        if (slidersData.length === 0) {
            alert('No slider data to export.');
            return;
        }

        slidersData = slidersData.map(slider => {
            const sliderGroup = Array.from(slidersContainer.children).find(group => group.querySelector('.slider-name').value === slider.name);
            const newValue = parseFloat(sliderGroup.querySelector('.slider').value);
            const newLeftText = sliderGroup.querySelector('.slider-left').value;
            const newRightText = sliderGroup.querySelector('.slider-right').value;
            return { name: slider.name, value: newValue, leftText: newLeftText, rightText: newRightText };
        });

        const jsonBlob = new Blob([JSON.stringify({ sliders: slidersData })], { type: 'application/json' });
        const url = URL.createObjectURL(jsonBlob);
        const link = document.createElement('a');
        link.href = url;
        link.download = 'sliders_data.json';
        link.click();
    });

    // Event: Reset data
    clearButton.addEventListener('click', function () {
        if (confirm('Wollen Sie wirklich alle Daten löschen?')) {
            slidersContainer.innerHTML = '';
            slidersData = [];
            initializeSliders();
        }
    });

    initializeSliders(); // Initialize with default values

// Ensure that the "Hattie" option is selected and trigger the button click on page load
window.addEventListener('DOMContentLoaded', function () {
    const jsonFileSelect = document.getElementById('jsonFileSelect');
    const loadJsonButton = document.getElementById('loadJsonButton');
    
    // Ensure the 'Hattie' option is selected by default
    jsonFileSelect.value = '..\\assets\\json\\hattie.json';

    // Simulate a click on the "Apply" button to trigger the action automatically
    loadJsonButton.click();
});

// Event listener for the button to load the selected JSON file (if needed)
document.getElementById('loadJsonButton').addEventListener('click', function () {
    const selectedFile = document.getElementById('jsonFileSelect').value;
    // Handle loading the JSON file or any other logic you need
    console.log('Selected JSON file:', selectedFile);
});

document.getElementById('printButton').addEventListener('click', function () {
    window.print();
});


});


