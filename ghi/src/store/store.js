import { configureStore } from '@reduxjs/toolkit';
import { setupListeners } from '@reduxjs/toolkit/query';
import { tokenApi } from './tokenApi';

export const store = configureStore({
  reducer: {
    [tokenApi.reducerPath]: tokenApi.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(tokenApi.middleware),
});

setupListeners(store.dispatch);
