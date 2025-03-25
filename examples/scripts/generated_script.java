
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.Keys;
import java.time.Duration;

public class GeneratedScript {
    public static void main(String[] args) {
        // Set up Chrome driver
        System.setProperty("webdriver.chrome.driver", "/path/to/chromedriver");
        WebDriver driver = new ChromeDriver();
        
        try {
            driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));

            // Perform actions
            driver.get("http://localhost:8080/");
            driver.findElement(By.xpath("```
//input[position()=1]
```")).sendKeys("admin");
            driver.findElement(By.xpath("(//input)[4]")).sendKeys("admin");
            driver.findElement(By.xpath("```
//button[contains(text(), 'Log in')][5]
```")).click();
            driver.findElement(By.xpath("```
//button[text()='All'][3]
```")).click();
            driver.findElement(By.xpath(""(//input)[3]"")).sendKeys("Workflow Studio");
            driver.findElement(By.tagName("body")).sendKeys(Keys.ENTER);
            System.out.println("✅ Successfully logged in and navigated to Workflow Studio.");

            driver.quit();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
