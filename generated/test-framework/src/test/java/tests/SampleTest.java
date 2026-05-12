package tests;

import base.BaseTest;
import org.testng.annotations.Test;

public class SampleTest extends BaseTest {

    @Test
    public void sampleTest() {

        driver.get("https://example.com");
    }
}