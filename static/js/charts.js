/**
 * Create a line chart using Chart.js
 * 
 * @param {string} canvasId - ID of the canvas element
 * @param {Array} labels - Array of labels for x-axis
 * @param {Array} datasets - Array of dataset objects
 * @param {boolean} hasMultipleYAxes - Whether chart has multiple y-axes
 */
function createLineChart(canvasId, labels, datasets, hasMultipleYAxes = false) {
    const ctx = document.getElementById(canvasId).getContext('2d');
    
    const options = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                position: 'top',
                labels: {
                    color: '#e0e0e0',
                    font: {
                        size: 12
                    }
                }
            },
            tooltip: {
                backgroundColor: 'rgba(0, 0, 0, 0.8)',
                bodyFont: {
                    size: 13
                },
                titleFont: {
                    size: 14
                }
            }
        },
        scales: {
            x: {
                grid: {
                    color: 'rgba(255, 255, 255, 0.05)'
                },
                ticks: {
                    color: '#999999'
                }
            },
            y: {
                grid: {
                    color: 'rgba(255, 255, 255, 0.05)'
                },
                ticks: {
                    color: '#999999'
                }
            }
        }
    };
    
    // Add second y-axis if needed
    if (hasMultipleYAxes) {
        options.scales.y1 = {
            type: 'linear',
            display: true,
            position: 'right',
            grid: {
                drawOnChartArea: false,
                color: 'rgba(255, 255, 255, 0.05)'
            },
            ticks: {
                color: '#999999'
            }
        };
    }
    
    return new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: datasets
        },
        options: options
    });
}

/**
 * Create a pie chart using Chart.js
 * 
 * @param {string} canvasId - ID of the canvas element
 * @param {Array} labels - Array of labels
 * @param {Array} data - Array of data values
 */
function createPieChart(canvasId, labels, data) {
    const ctx = document.getElementById(canvasId).getContext('2d');
    
    // Generate random colors for pie segments
    const backgroundColors = labels.map(() => 
        `hsl(${Math.floor(Math.random() * 360)}, 70%, 60%)`
    );
    
    return new Chart(ctx, {
        type: 'pie',
        data: {
            labels: labels,
            datasets: [{
                data: data,
                backgroundColor: backgroundColors,
                borderWidth: 1,
                borderColor: '#252636'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'right',
                    labels: {
                        color: '#e0e0e0',
                        font: {
                            size: 12
                        },
                        padding: 15
                    }
                },
                tooltip: {
                    backgroundColor: 'rgba(0, 0, 0, 0.8)',
                    bodyFont: {
                        size: 13
                    },
                    titleFont: {
                        size: 14
                    }
                }
            }
        }
    });
}

/**
 * Create a comparison chart for actual vs forecast data
 * 
 * @param {string} canvasId - ID of the canvas element
 * @param {Array} labels - Array of date labels
 * @param {Array} datasets - Array of dataset objects
 * @param {string} yAxisPrefix - Prefix for y-axis labels (e.g. '$')
 */
function createComparisonChart(canvasId, labels, datasets, yAxisPrefix = '') {
    const ctx = document.getElementById(canvasId).getContext('2d');
    
    return new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: datasets
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            interaction: {
                mode: 'index',
                intersect: false
            },
            plugins: {
                legend: {
                    position: 'top',
                    labels: {
                        color: '#e0e0e0',
                        font: {
                            size: 12
                        }
                    }
                },
                tooltip: {
                    backgroundColor: 'rgba(0, 0, 0, 0.8)',
                    bodyFont: {
                        size: 13
                    },
                    titleFont: {
                        size: 14
                    },
                    callbacks: {
                        label: function(context) {
                            let label = context.dataset.label || '';
                            if (label) {
                                label += ': ';
                            }
                            if (context.parsed.y !== null) {
                                label += yAxisPrefix + context.parsed.y;
                            }
                            return label;
                        }
                    }
                }
            },
            scales: {
                x: {
                    grid: {
                        color: 'rgba(255, 255, 255, 0.05)'
                    },
                    ticks: {
                        color: '#999999',
                        maxRotation: 45,
                        minRotation: 45
                    }
                },
                y: {
                    grid: {
                        color: 'rgba(255, 255, 255, 0.05)'
                    },
                    ticks: {
                        color: '#999999',
                        callback: function(value) {
                            return yAxisPrefix + value;
                        }
                    }
                }
            }
        }
    });
}
