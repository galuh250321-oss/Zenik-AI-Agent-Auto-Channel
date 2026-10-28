import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// Local port is used by the development toolchain only. The installed .exe
// bundles static frontend assets and does not open a localhost dashboard.
export default defineConfig({
  plugins: [react()],
  clearScreen: false,
  server: { host: "127.0.0.1", port: 5173, strictPort: true },
});
