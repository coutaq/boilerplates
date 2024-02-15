import axios from "axios";
import { useStorage } from "@vueuse/core";

const baseURL = import.meta.env.VITE_API_URL;

export function useApi() {
    const api = axios.create({
    baseURL,
    });

    api.defaults.headers.common["Accept"] = "application/json";
    api.defaults.headers.common["Authorization"] = `Bearer ${
    useStorage("token", null).value
    }`;

    return api
}