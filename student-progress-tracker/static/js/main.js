/*
 * Student Progress Tracker - Main JavaScript
 * Core functionality and utilities
 */

// Utility functions
const Utils = {
    // Show loading state
    showLoading(element) {
        if (element) {
            element.classList.add('loading');
        }
    },

    // Hide loading state
    hideLoading(element) {
        if (element) {
            element.classList.remove('loading');
        }
    },

    // Show toast notification
    showToast(message, type = 'info') {
        // Create toast element
        const toast = document.createElement('div');
        toast.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
        toast.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
        toast.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        document.body.appendChild(toast);

        // Auto remove after 5 seconds
        setTimeout(() => {
            if (toast.parentNode) {
                toast.parentNode.removeChild(toast);
            }
        }, 5000);
    },

    // Format date
    formatDate(dateString) {
        const date = new Date(dateString);
        return date.toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'short',
            day: 'numeric'
        });
    },

    // Calculate percentage
    calculatePercentage(value, total) {
        if (total === 0) return 0;
        return Math.round((value / total) * 100);
    },

    // Debounce function
    debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
};

// Form validation
const FormValidator = {
    validateEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    },

    validatePassword(password) {
        return password.length >= 6;
    },

    validateForm(formId) {
        const form = document.getElementById(formId);
        if (!form) return false;

        let isValid = true;
        const emailInputs = form.querySelectorAll('input[type="email"]');
        const passwordInputs = form.querySelectorAll('input[type="password"]');

        // Validate email fields
        emailInputs.forEach(input => {
            if (!this.validateEmail(input.value)) {
                this.showError(input, 'Please enter a valid email address');
                isValid = false;
            } else {
                this.clearError(input);
            }
        });

        // Validate password fields
        passwordInputs.forEach(input => {
            if (!this.validatePassword(input.value)) {
                this.showError(input, 'Password must be at least 6 characters long');
                isValid = false;
            } else {
                this.clearError(input);
            }
        });

        return isValid;
    },

    showError(input, message) {
        input.classList.add('is-invalid');
        let errorDiv = input.parentElement.querySelector('.invalid-feedback');
        if (!errorDiv) {
            errorDiv = document.createElement('div');
            errorDiv.className = 'invalid-feedback';
            input.parentElement.appendChild(errorDiv);
        }
        errorDiv.textContent = message;
    },

    clearError(input) {
        input.classList.remove('is-invalid');
        const errorDiv = input.parentElement.querySelector('.invalid-feedback');
        if (errorDiv) {
            errorDiv.remove();
        }
    }
};

// Chart utilities
const ChartUtils = {
    createLineChart(canvasId, labels, data, label) {
        const ctx = document.getElementById(canvasId);
        if (!ctx) return null;

        return new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: label,
                    data: data,
                    borderColor: 'rgb(52, 152, 219)',
                    backgroundColor: 'rgba(52, 152, 219, 0.1)',
                    tension: 0.4,
                    fill: true
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 100
                    }
                }
            }
        });
    },

    createDoughnutChart(canvasId, labels, data, colors) {
        const ctx = document.getElementById(canvasId);
        if (!ctx) return null;

        return new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: labels,
                datasets: [{
                    data: data,
                    backgroundColor: colors || ['#28a745', '#dc3545', '#ffc107', '#17a2b8']
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false
            }
        });
    }
};

// Initialize on DOM load
document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Form validation on submit
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (form.id && !FormValidator.validateForm(form.id)) {
                e.preventDefault();
                Utils.showToast('Please correct the errors in the form', 'danger');
            }
        });
    });

    // Auto-hide alerts after 5 seconds
    setTimeout(function() {
        const alerts = document.querySelectorAll('.alert');
        alerts.forEach(alert => {
            if (alert.classList.contains('alert-dismissible')) {
                alert.style.transition = 'opacity 0.5s';
                alert.style.opacity = '0';
                setTimeout(() => {
                    if (alert.parentNode) {
                        alert.parentNode.removeChild(alert);
                    }
                }, 500);
            }
        });
    }, 5000);

    // Add loading animation to buttons on click
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            if (button.type === 'submit') {
                button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Loading...';
                button.disabled = true;

                // Re-enable after 3 seconds (fallback)
                setTimeout(() => {
                    button.disabled = false;
                }, 3000);
            }
        });
    });
});

// Global functions
window.Utils = Utils;
window.FormValidator = FormValidator;
window.ChartUtils = ChartUtils;

// Show success message
window.showSuccess = function(message) {
    Utils.showToast(message, 'success');
};

// Show error message
window.showError = function(message) {
    Utils.showToast(message, 'danger');
};

// Show info message
window.showInfo = function(message) {
    Utils.showToast(message, 'info');
};
