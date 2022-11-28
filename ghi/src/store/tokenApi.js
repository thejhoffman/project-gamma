import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

export const tokenApi = createApi({
  reducerPath: "token",
  baseQuery: fetchBaseQuery({
    baseUrl: process.env.REACT_APP_SAMPLE_SERVICE_API_HOST,
    credentials: 'include'
  }),
  tagTypes: ['AccountAuth'],
  endpoints: builder => ({
    getToken: builder.query({
      query: () => '/token',
      providesTags: ['AccountAuth'],
    }),
    loginAccount: builder.mutation({
      query: data => ({
        url: '/token',
        headers: {
          'content-type': 'application/x-www-form-urlencoded',
        },
        body: data,
        method: 'post',
      }),
      invalidatesTags: ['AccountAuth'],
    }),
    logoutAccount: builder.mutation({
      query: () => ({
        url: '/token',
        method: 'delete'
      }),
      invalidatesTags: ['AccountAuth'],
    })
  })
});

export const {
  useGetTokenQuery,
  useLoginAccountMutation,
  useLogoutAccountMutation,
} = tokenApi;
