"""
WebDriver Setup Module
======================
Professional WebDriver factory for Selenium automation.
Supports Chrome, Firefox, and Edge browsers with configurable options.

Author: Muhammad Yasin Asif
Portfolio: QA Engineer Portfolio
"""

import os
import yaml
from typing import Optional
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class DriverFactory:
    """
    Factory class for creating WebDriver instances.
    
    Supports multiple browsers and configurations.
    Uses webdriver-manager for automatic driver management.
    """
    
    SUPPORTED_BROWSERS = ['chrome', 'firefox', 'edge']
    
    def __init__(self, config_path: str = 'config.yaml'):
        """
        Initialize DriverFactory with configuration.
        
        Args:
            config_path: Path to the YAML configuration file
        """
        self.config = self._load_config(config_path)
        self.driver: Optional[webdriver.Remote] = None
        
    def _load_config(self, config_path: str) -> dict:
        """Load configuration from YAML file."""
        try:
            with open(config_path, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            print(f"Config file not found: {config_path}. Using defaults.")
            return self._get_default_config()
    
    def _get_default_config(self) -> dict:
        """Return default configuration if config file not found."""
        return {
            'browser': {
                'name': 'chrome',
                'headless': False,
                'maximize': True,
                'implicit_wait': 10,
                'page_load_timeout': 30,
            },
            'environments': {
                'dev': {'base_url': 'https://www.saucedemo.com'}
            },
            'default_environment': 'dev'
        }
    
    def create_driver(self, browser_name: Optional[str] = None, 
                      headless: Optional[bool] = None) -> webdriver.Remote:
        """
        Create and return a WebDriver instance.
        
        Args:
            browser_name: Browser to use (chrome, firefox, edge)
            headless: Run in headless mode
            
        Returns:
            WebDriver instance
        """
        browser = browser_name or self.config.get('browser', {}).get('name', 'chrome')
        browser = browser.lower()
        
        if browser not in self.SUPPORTED_BROWSERS:
            raise ValueError(f"Browser '{browser}' not supported. "
                           f"Use one of: {self.SUPPORTED_BROWSERS}")
        
        is_headless = headless if headless is not None else \
                      self.config.get('browser', {}).get('headless', False)
        
        if browser == 'chrome':
            self.driver = self._create_chrome_driver(is_headless)
        elif browser == 'firefox':
            self.driver = self._create_firefox_driver(is_headless)
        elif browser == 'edge':
            self.driver = self._create_edge_driver(is_headless)
            
        self._configure_driver()
        return self.driver
    
    def _create_chrome_driver(self, headless: bool) -> webdriver.Chrome:
        """Create Chrome WebDriver instance."""
        options = ChromeOptions()
        
        if headless:
            options.add_argument('--headless=new')
            
        # Add Chrome options from config
        chrome_options = self.config.get('browser', {}).get('chrome_options', [])
        for opt in chrome_options:
            options.add_argument(opt)
            
        # Common options for stability
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        
        service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)
    
    def _create_firefox_driver(self, headless: bool) -> webdriver.Firefox:
        """Create Firefox WebDriver instance."""
        options = FirefoxOptions()
        
        if headless:
            options.add_argument('--headless')
            
        service = FirefoxService(GeckoDriverManager().install())
        return webdriver.Firefox(service=service, options=options)
    
    def _create_edge_driver(self, headless: bool) -> webdriver.Edge:
        """Create Edge WebDriver instance."""
        options = EdgeOptions()
        
        if headless:
            options.add_argument('--headless')
            
        service = EdgeService(EdgeChromiumDriverManager().install())
        return webdriver.Edge(service=service, options=options)
    
    def _configure_driver(self):
        """Configure driver with timeouts and window settings."""
        browser_config = self.config.get('browser', {})
        
        # Set implicit wait
        implicit_wait = browser_config.get('implicit_wait', 10)
        self.driver.implicitly_wait(implicit_wait)
        
        # Set page load timeout
        page_load_timeout = browser_config.get('page_load_timeout', 30)
        self.driver.set_page_load_timeout(page_load_timeout)
        
        # Maximize window if configured
        if browser_config.get('maximize', True):
            self.driver.maximize_window()
    
    def get_base_url(self, environment: Optional[str] = None) -> str:
        """
        Get base URL for the specified environment.
        
        Args:
            environment: Environment name (dev, qa, staging, prod)
            
        Returns:
            Base URL string
        """
        env = environment or self.config.get('default_environment', 'dev')
        environments = self.config.get('environments', {})
        return environments.get(env, {}).get('base_url', 'https://www.saucedemo.com')
    
    def quit_driver(self):
        """Safely quit the WebDriver instance."""
        if self.driver:
            try:
                self.driver.quit()
            except Exception as e:
                print(f"Error quitting driver: {e}")
            finally:
                self.driver = None


def get_driver(browser: str = 'chrome', headless: bool = False) -> webdriver.Remote:
    """
    Convenience function to quickly get a WebDriver instance.
    
    Args:
        browser: Browser name (chrome, firefox, edge)
        headless: Run in headless mode
        
    Returns:
        WebDriver instance
    """
    factory = DriverFactory()
    return factory.create_driver(browser_name=browser, headless=headless)


# Example usage
if __name__ == '__main__':
    # Quick test
    print("Testing WebDriver setup...")
    
    factory = DriverFactory()
    driver = factory.create_driver()
    
    base_url = factory.get_base_url()
    driver.get(base_url)
    
    print(f"Opened: {driver.title}")
    print(f"URL: {driver.current_url}")
    
    factory.quit_driver()
    print("WebDriver test complete!")
