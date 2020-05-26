'''
from selenium import webdriver
import zxing

driver=webdriver.Chrome()
driver.get("https://barcode.tec-it.com/en")
driver.maximize_window()
driver.implicitly_wait(6)
C:\\Users\\Manoj\\Desktop\\Mbarcode.gif
barcodeURL=driver.find_element_by_tag_name("img").get_attribute("src")
print (barcodeURL)
'''


#https://www.google.com/search?q=price+barcode+images&tbm=isch&source=iu&ictx=1&fir=-rBRMaplerp6XM%253A%252C_rfFzt0lvuBZvM%252C_&vet=1&usg=AI4_-kRV34zPuXtS-6LZ2xPj7ocpvqRMqw&sa=X&ved=2ahUKEwj3hfrXy9ToAhWDILcAHcfYB-AQ9QEwAHoECAoQFw#imgrc=QpNJmGeuO05W6M
'''
import zxing
reader = zxing.BarCodeReader()
barcode = reader.decode("C:\\Users\\Manoj\\Desktop\\xyz.jpg")
print (barcode)
print(barcode.raw)
if barcode.raw == "01234565":
    print ("Test is passed ...")
else:
    print ("Test is failed ...")
'''

import urllib.request
from selenium import webdriver
import zxing
import requests
driver=webdriver.Chrome()
driver.get("https://barcode.tec-it.com/en")
driver.maximize_window()
driver.implicitly_wait(6)
barcodeURL=driver.find_element_by_tag_name("img").get_attribute("src")
print (barcodeURL)
#weburl=urllib.request.urlopen(barcodeURL)
response=requests.get(barcodeURL)
for i in response:
    print (i)




'''
import zxing
reader = zxing.BarCodeReader()
barcode = reader.decode("C:\\Users\\Manoj\\Desktop\\Mbarcode.gif")
print(barcode)

if barcode.raw == "Manoj Is Trying":
    print ("Test is passed ...")
else:
    print ("Test is failed ...")
'''
'''
package
practiceTest;

import java.awt.image.BufferedImage;
import java.io.IOException;
import java.net.URL;
import javax.imageio.ImageIO;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import com.google.zxing.BinaryBitmap;
import com.google.zxing.LuminanceSource;
import com.google.zxing.MultiFormatReader;
import com.google.zxing.NotFoundException;
import com.google.zxing.Result;
import com.google.zxing.client.j2se.BufferedImageLuminanceSource;
import com.google.zxing.common.HybridBinarizer;

public


class BarCode_Reader
    {
        public
    static
    void
    main(String[]
    args) throws
    IOException, NotFoundException
    {
        System.setProperty("webdriver.chrome.driver", "D://Chrome Driver 2.38//chromedriver_win32//chromedriver.exe");
    WebDriver
    driver = new
    ChromeDriver();

    driver.get("https://worldbarcodes.com/sample-barcode-images/");
    driver.manage().window().maximize();
    String
    barCodeURL = driver.findElement(By.xpath("//img[@title='EAN-13 barcode image']")).getAttribute("src");

    System.out.println(barCodeURL);
    URL
    url = new
    URL(barCodeURL);
    BufferedImage
    bufferedimage = ImageIO.read(url);
    LuminanceSource
    luminanceSource = new
    BufferedImageLuminanceSource(bufferedimage);
    BinaryBitmap
    binaryBitmap = new
    BinaryBitmap(new
    HybridBinarizer(luminanceSource));
    Result
    result = new
    MultiFormatReader().decode(binaryBitmap);
    System.out.println(result.getText());
    System.out.println("Test Completed");
    driver.quit();
    }
    }

'''

'''
import zxing
reader = zxing.BarCodeReader()
barcode = reader.decode("C:\\Users\\Manoj\\Desktop\\Mbarcode.gif")
print(barcode)
print (barcode.raw)

if barcode.raw == "Manoj Is Trying":
    print ("Test is passed ...")
else:
    print ("Test is failed ...")

'''