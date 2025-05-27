/**
 * Dashboard JavaScript functionality
 */
document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize popovers
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function(popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Auto-submit forms when brand selection changes
    const brandSelects = document.querySelectorAll('select[name="brand_id"]');
    brandSelects.forEach(select => {
        select.addEventListener('change', function() {
            // Clear product selection when brand changes
            const productSelect = this.form.querySelector('select[name="product_id"]');
            if (productSelect) {
                productSelect.value = '';
            }
            
            // Submit the form
            this.form.submit();
        });
    });

    // Track active tab in URL
    const triggerTabList = [].slice.call(document.querySelectorAll('a[data-bs-toggle="tab"], button[data-bs-toggle="tab"]'));
    triggerTabList.forEach(function(triggerEl) {
        const tabTrigger = new bootstrap.Tab(triggerEl);
        
        triggerEl.addEventListener('click', function(event) {
            event.preventDefault();
            tabTrigger.show();
            
            // Update URL with tab ID
            const tabId = this.getAttribute('data-bs-target').substring(1);
            updateUrlParam('tab', tabId);
        });
    });
    
    // Activate tab from URL param
    const urlParams = new URLSearchParams(window.location.search);
    const tabParam = urlParams.get('tab');
    if (tabParam) {
        const tab = document.querySelector(`[data-bs-target="#${tabParam}"]`);
        if (tab) {
            new bootstrap.Tab(tab).show();
        }
    }
    
    // Add date range validation
    const startDateInput = document.getElementById('start_date');
    const endDateInput = document.getElementById('end_date');
    
    if (startDateInput && endDateInput) {
        startDateInput.addEventListener('change', validateDateRange);
        endDateInput.addEventListener('change', validateDateRange);
    }
    
    function validateDateRange() {
        if (startDateInput.value && endDateInput.value) {
            const startDate = new Date(startDateInput.value);
            const endDate = new Date(endDateInput.value);
            
            if (startDate > endDate) {
                alert('Start date cannot be after end date');
                endDateInput.value = startDateInput.value;
            }
        }
    }
    
    // Helper function to update URL parameters
    function updateUrlParam(key, value) {
        const url = new URL(window.location.href);
        url.searchParams.set(key, value);
        window.history.replaceState({}, '', url);
    }
});

/**
 * Format number with commas and decimal places
 * 
 * @param {number} number - Number to format
 * @param {number} decimals - Number of decimal places
 * @returns {string} Formatted number
 */
function formatNumber(number, decimals = 0) {
    return number.toFixed(decimals).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

/**
 * Format currency
 * 
 * @param {number} amount - Amount to format
 * @returns {string} Formatted currency
 */
function formatCurrency(amount) {
    return '$' + formatNumber(amount, 2);
}
