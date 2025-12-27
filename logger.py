"""
Logger Module
=============
Professional logging configuration for test automation framework.
Provides both console and file logging with rotation support.

Author: Muhammad Yasin Asif
Portfolio: QA Engineer Portfolio
"""

import os
import logging
import yaml
from datetime import datetime
from logging.handlers import RotatingFileHandler
from typing import Optional


class TestLogger:
    """
    Custom logger class for test automation.
    
    Features:
    - Console and file logging
    - Log rotation
    - Customizable formats
    - Test step logging
    """
    
    _instances = {}
    
    def __new__(cls, name: str = 'TestLogger', config_path: str = 'config.yaml'):
        """Singleton pattern - one logger per name."""
        if name not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[name] = instance
        return cls._instances[name]
    
    def __init__(self, name: str = 'TestLogger', config_path: str = 'config.yaml'):
        """
        Initialize the logger with configuration.
        
        Args:
            name: Logger name
            config_path: Path to YAML configuration file
        """
        if hasattr(self, '_initialized'):
            return
            
        self._initialized = True
        self.name = name
        self.config = self._load_config(config_path)
        self.logger = self._setup_logger()
        
    def _load_config(self, config_path: str) -> dict:
        """Load logging configuration from YAML file."""
        try:
            with open(config_path, 'r') as file:
                config = yaml.safe_load(file)
                return config.get('logging', self._get_default_config())
        except FileNotFoundError:
            return self._get_default_config()
    
    def _get_default_config(self) -> dict:
        """Return default logging configuration."""
        return {
            'level': 'INFO',
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'file_name': 'test_execution.log',
            'log_dir': 'logs',
            'max_bytes': 10485760,  # 10MB
            'backup_count': 5
        }
    
    def _setup_logger(self) -> logging.Logger:
        """Configure and return logger instance."""
        logger = logging.getLogger(self.name)
        
        # Clear existing handlers
        logger.handlers = []
        
        # Set log level
        level = getattr(logging, self.config.get('level', 'INFO').upper())
        logger.setLevel(level)
        
        # Create formatters
        log_format = self.config.get(
            'format', 
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        formatter = logging.Formatter(log_format)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        # File handler with rotation
        log_dir = self.config.get('log_dir', 'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        log_file = os.path.join(log_dir, self.config.get('file_name', 'test_execution.log'))
        
        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=self.config.get('max_bytes', 10485760),
            backupCount=self.config.get('backup_count', 5)
        )
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
        return logger
    
    def info(self, message: str):
        """Log info level message."""
        self.logger.info(message)
    
    def debug(self, message: str):
        """Log debug level message."""
        self.logger.debug(message)
    
    def warning(self, message: str):
        """Log warning level message."""
        self.logger.warning(message)
    
    def error(self, message: str):
        """Log error level message."""
        self.logger.error(message)
    
    def critical(self, message: str):
        """Log critical level message."""
        self.logger.critical(message)
    
    def step(self, step_number: int, description: str):
        """
        Log a test step.
        
        Args:
            step_number: Step number in the test
            description: Step description
        """
        self.logger.info(f"[STEP {step_number}] {description}")
    
    def test_start(self, test_name: str):
        """Log test start."""
        self.logger.info("=" * 60)
        self.logger.info(f"TEST START: {test_name}")
        self.logger.info("=" * 60)
    
    def test_pass(self, test_name: str):
        """Log test pass."""
        self.logger.info(f"✅ TEST PASSED: {test_name}")
        self.logger.info("-" * 60)
    
    def test_fail(self, test_name: str, error: Optional[str] = None):
        """Log test failure."""
        self.logger.error(f"❌ TEST FAILED: {test_name}")
        if error:
            self.logger.error(f"Error: {error}")
        self.logger.info("-" * 60)
    
    def test_skip(self, test_name: str, reason: str):
        """Log test skip."""
        self.logger.warning(f"⏭️ TEST SKIPPED: {test_name} - Reason: {reason}")
        self.logger.info("-" * 60)


def get_logger(name: str = 'TestLogger') -> TestLogger:
    """
    Get a logger instance.
    
    Args:
        name: Logger name
        
    Returns:
        TestLogger instance
    """
    return TestLogger(name)


# Convenience function for quick logging
def log_info(message: str):
    """Quick info logging."""
    get_logger().info(message)


def log_error(message: str):
    """Quick error logging."""
    get_logger().error(message)


def log_step(step_number: int, description: str):
    """Quick step logging."""
    get_logger().step(step_number, description)


# Example usage
if __name__ == '__main__':
    # Test the logger
    logger = get_logger('TestExample')
    
    logger.test_start('Sample Login Test')
    logger.step(1, 'Navigate to login page')
    logger.step(2, 'Enter username')
    logger.step(3, 'Enter password')
    logger.step(4, 'Click login button')
    logger.info('Login successful')
    logger.test_pass('Sample Login Test')
    
    print("\nLogger test complete! Check logs/ directory for log file.")
