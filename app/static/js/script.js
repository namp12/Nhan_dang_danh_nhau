// Violence Detection System - Frontend JavaScript

// Modal functionality
const modal = document.getElementById('addCameraModal');
const addCameraBtn = document.getElementById('addCameraBtn');
const cancelBtn = document.getElementById('cancelBtn');
const closeBtn = document.getElementsByClassName('close')[0];

if (addCameraBtn) {
    addCameraBtn.onclick = function() {
        modal.style.display = 'block';
    }
}

if (cancelBtn) {
    cancelBtn.onclick = function() {
        modal.style.display = 'none';
    }
}

if (closeBtn) {
    closeBtn.onclick = function() {
        modal.style.display = 'none';
    }
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}

// Add Camera Form
const addCameraForm = document.getElementById('addCameraForm');
if (addCameraForm) {
    addCameraForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const formData = new FormData(this);
        const cameraData = Object.fromEntries(formData.entries());
        
        try {
            const response = await fetch('/api/cameras', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(cameraData)
            });
            
            if (response.ok) {
                alert('Camera added successfully!');
                modal.style.display = 'none';
                this.reset();
                loadCameras();
            } else {
                alert('Failed to add camera');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error adding camera');
        }
    });
}

// Load cameras
async function loadCameras() {
    try {
        const response = await fetch('/api/cameras');
        const data = await response.json();
        
        const cameraGrid = document.getElementById('cameraGrid');
        if (cameraGrid && data.cameras.length > 0) {
            cameraGrid.innerHTML = data.cameras.map(camera => `
                <div class="camera-item">
                    <div class="camera-feed">
                        <div class="no-feed">
                            <p>${camera.name}</p>
                            <p class="hint">${camera.location || 'No location set'}</p>
                        </div>
                    </div>
                </div>
            `).join('');
        }
    } catch (error) {
        console.error('Error loading cameras:', error);
    }
}

// Detection Config Form
const detectionConfigForm = document.getElementById('detectionConfigForm');
if (detectionConfigForm) {
    const confidenceThreshold = document.getElementById('confidenceThreshold');
    const rangeValue = document.querySelector('.range-value');
    
    if (confidenceThreshold && rangeValue) {
        confidenceThreshold.addEventListener('input', function() {
            rangeValue.textContent = this.value + '%';
        });
    }
    
    detectionConfigForm.addEventListener('submit', function(e) {
        e.preventDefault();
        alert('Detection settings saved!');
    });
}

// Alert Config Form
const alertConfigForm = document.getElementById('alertConfigForm');
if (alertConfigForm) {
    alertConfigForm.addEventListener('submit', function(e) {
        e.preventDefault();
        alert('Alert settings saved!');
    });
}

// Storage Config Form
const storageConfigForm = document.getElementById('storageConfigForm');
if (storageConfigForm) {
    storageConfigForm.addEventListener('submit', function(e) {
        e.preventDefault();
        alert('Storage settings saved!');
    });
}

// Filter functionality
const applyFilters = document.getElementById('applyFilters');
if (applyFilters) {
    applyFilters.addEventListener('click', function() {
        const filterDate = document.getElementById('filterDate').value;
        const filterCamera = document.getElementById('filterCamera').value;
        const filterStatus = document.getElementById('filterStatus').value;
        
        console.log('Applying filters:', { filterDate, filterCamera, filterStatus });
        // TODO: Implement actual filtering logic
    });
}

// View detection details
document.addEventListener('click', function(e) {
    if (e.target.classList.contains('btn-view')) {
        const recordId = e.target.getAttribute('data-id');
        alert('Viewing detection record: ' + recordId);
        // TODO: Implement modal to show detection details
    }
});

// Update dashboard stats (placeholder)
function updateDashboardStats() {
    // TODO: Fetch real data from API
    const stats = {
        activeCameras: 0,
        detectionsToday: 0,
        accuracy: 98.5,
        status: 'Active'
    };
    
    const activeCamerasEl = document.getElementById('activeCameras');
    const detectionsTodayEl = document.getElementById('detectionsToday');
    const accuracyEl = document.getElementById('accuracy');
    
    if (activeCamerasEl) activeCamerasEl.textContent = stats.activeCameras;
    if (detectionsTodayEl) detectionsTodayEl.textContent = stats.detectionsToday;
    if (accuracyEl) accuracyEl.textContent = stats.accuracy + '%';
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    updateDashboardStats();
    
    if (document.getElementById('cameraGrid')) {
        loadCameras();
    }
});

// Auto-refresh dashboard every 30 seconds
setInterval(updateDashboardStats, 30000);
