
import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './src/tests',
  retries: 1,
  use: {
    headless: true,
    screenshot: 'only-on-failure'
  }
});
